"""Capture genuine SDK RichPreviewer frames and inspector output on Windows.

The real SDK renderer creates its hidden GLFW surface. This helper implements
the IDE's documented local transports; it does not implement or mock ArkUI.
Usage: python capture_native_arkui_previewer.py --previewer PATH --output DIR
       --timeout 45 -- [the RichPreviewer arguments except -s and -lws]
"""
import argparse
import datetime
import hashlib
import io
import json
import os
from pathlib import Path
import socket
import struct
import subprocess
import threading
import time
import uuid

import websocket
import win32file
import win32pipe
import pywintypes
from PIL import Image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previewer', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--timeout', type=float, default=45)
    parser.add_argument('renderer_args', nargs=argparse.REMAINDER)
    options = parser.parse_args()
    forwarded = options.renderer_args
    if forwarded and forwarded[0] == '--':
        forwarded = forwarded[1:]
    if any(value in ('-s', '-lws') for value in forwarded):
        parser.error('The helper assigns -s and -lws locally.')
    previewer = options.previewer.resolve(strict=True)
    output = options.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    pipe_base = 'arkts_corpus_' + uuid.uuid4().hex
    pipe_path = '\\\\.\\pipe\\' + pipe_base + '_commandPipe'
    pipe = win32pipe.CreateNamedPipe(
        pipe_path, win32pipe.PIPE_ACCESS_DUPLEX,
        win32pipe.PIPE_TYPE_BYTE | win32pipe.PIPE_READMODE_BYTE | win32pipe.PIPE_WAIT,
        1, 262144, 262144, 0, None,
    )
    pipe_messages = []
    pipe_errors = []
    connected = threading.Event()
    stopped = threading.Event()

    def read_pipe():
        accumulated = b''
        try:
            try:
                win32pipe.ConnectNamedPipe(pipe, None)
            except pywintypes.error as error:
                if error.winerror != 535:  # Client connected before ConnectNamedPipe.
                    raise
            connected.set()
            while not stopped.is_set():
                _, fragment = win32file.ReadFile(pipe, 65536)
                if not fragment:
                    break
                accumulated += fragment
                while b'\x00' in accumulated:
                    message, accumulated = accumulated.split(b'\x00', 1)
                    raw = message.decode('utf-8', errors='replace')
                    try:
                        parsed = json.loads(raw)
                    except json.JSONDecodeError:
                        parsed = {'raw': raw}
                    pipe_messages.append(parsed)
        except pywintypes.error as error:
            if not stopped.is_set():
                pipe_errors.append(str(error))

    pipe_thread = threading.Thread(target=read_pipe, daemon=True)
    pipe_thread.start()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as candidate:
        candidate.bind(('127.0.0.1', 0))
        port = candidate.getsockname()[1]
    command = [str(previewer), *forwarded, '-s', pipe_base, '-lws', str(port)]
    started = time.monotonic()
    log_path = output / 'previewer.log'
    capture_error = None
    frame_info = None
    frame_count = 0
    first_frame_at = None
    connection = None
    process = None
    return_code_before_stop = None
    with log_path.open('wb') as log:
        try:
            process = subprocess.Popen(
                command, cwd=previewer.parent, stdout=log, stderr=subprocess.STDOUT,
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
            while time.monotonic() - started < options.timeout:
                if process.poll() is not None:
                    return_code_before_stop = process.returncode
                    raise RuntimeError(f'Previewer exited before receiving a frame: {process.returncode}')
                try:
                    connection = websocket.create_connection(
                        f'ws://127.0.0.1:{port}/', timeout=0.6,
                        subprotocols=['ws'], http_proxy_host=None,
                    )
                    break
                except (OSError, websocket.WebSocketException):
                    time.sleep(0.15)
            if connection is None:
                raise TimeoutError('No local renderer WebSocket became available.')
            while time.monotonic() - started < options.timeout:
                if frame_info is not None:
                    inspector_now = json.dumps([
                        m for m in pipe_messages if isinstance(m, dict) and m.get('command') == 'inspector'
                    ], ensure_ascii=False)
                    if 'Hello, World!' in inspector_now and time.monotonic() - first_frame_at >= 0.4:
                        break
                    if time.monotonic() - first_frame_at >= 6:
                        break
                try:
                    received = connection.recv()
                except websocket.WebSocketTimeoutException:
                    continue
                if not isinstance(received, bytes) or len(received) <= 40:
                    continue
                if frame_count == 0:
                    (output / 'first-native-packet.bin').write_bytes(received)
                    (output / 'first-native-packet-header.json').write_text(json.dumps({
                        'packet_bytes': len(received), 'header_hex': received[:40].hex(),
                        'network_order_header': list(struct.unpack_from('>IIIII', received)),
                    }, indent=2), encoding='utf-8')
                # Official VirtualScreenImpl::WriteBuffer uses ToNetworkEndian.
                magic, width, height, compressed_width, compressed_height = struct.unpack_from('>IIIII', received)
                if magic != 0x12345678:
                    raise ValueError(f'Unexpected native frame header: {magic:#x}')
                payload = received[40:]
                image = Image.open(io.BytesIO(payload))
                image.load()
                if image.format != 'JPEG' or image.size != (width, height):
                    raise ValueError('The native JPEG dimensions do not match the transport header.')
                frame_count += 1
                if first_frame_at is None:
                    first_frame_at = time.monotonic()
                    (output / 'first-native-frame.jpg').write_bytes(payload)
                (output / 'native-frame.bin').write_bytes(received)
                frame_path = output / 'native-frame.jpg'
                frame_path.write_bytes(payload)
                frame_info = {
                    'path': str(frame_path), 'transport_bytes': len(received),
                    'jpeg_bytes': len(payload), 'width': width, 'height': height,
                    'compression_width': compressed_width, 'compression_height': compressed_height,
                    'jpeg_sha256': hashlib.sha256(payload).hexdigest(),
                    'frame_number': frame_count,
                    'pixel_channel_extrema': image.getextrema(),
                }
            if frame_info is None:
                raise TimeoutError('The native renderer did not send a valid frame before the deadline.')
            inspector_deadline = min(started + options.timeout, time.monotonic() + 4)
            while time.monotonic() < inspector_deadline:
                if any(m.get('command') == 'inspector' for m in pipe_messages if isinstance(m, dict)):
                    break
                time.sleep(0.1)
        except Exception as error:
            capture_error = f'{type(error).__name__}: {error}'
        finally:
            if connection is not None:
                connection.close()
            stopped.set()
            if process is not None:
                return_code_before_stop = process.poll()
                if return_code_before_stop is None:
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=5)
            try:
                win32pipe.DisconnectNamedPipe(pipe)
            except pywintypes.error:
                pass
            win32file.CloseHandle(pipe)
            pipe_thread.join(timeout=1)
    inspectors = [m for m in pipe_messages if isinstance(m, dict) and m.get('command') == 'inspector']
    for inspector in inspectors:
        if isinstance(inspector.get('result'), str):
            try:
                inspector['parsed_result'] = json.loads(inspector['result'])
            except json.JSONDecodeError:
                pass
    (output / 'native-inspector.json').write_text(
        json.dumps(inspectors, ensure_ascii=False, indent=2), encoding='utf-8',
    )
    (output / 'command-pipe-messages.json').write_text(
        json.dumps(pipe_messages, ensure_ascii=False, indent=2), encoding='utf-8',
    )
    inspector_text = json.dumps(inspectors, ensure_ascii=False)
    receipt = {
        'observed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'real_sdk_previewer': str(previewer),
        'command': command, 'working_directory': str(previewer.parent),
        'transport': 'Windows local named pipe and localhost WebSocket',
        'frame': frame_info, 'named_pipe_connected': connected.is_set(),
        'native_frame_count_received': frame_count,
        'frame_header_byte_order': 'network big endian',
        'inspector_message_count': len(inspectors),
        'hello_world_in_native_inspector': 'Hello, World!' in inspector_text,
        'capture_error': capture_error, 'pipe_errors': pipe_errors,
        'process_id': process.pid if process else None,
        'renderer_exit_code_before_cleanup': return_code_before_stop,
        'renderer_exit_code_after_cleanup': process.returncode if process else None,
        'renderer_stopped': process is not None and process.poll() is not None,
        'elapsed_seconds': round(time.monotonic() - started, 3),
        'log_path': str(log_path),
        'interpretation': 'A frame proves native rendering. Hello World semantics also require matching inspector content or visual inspection of the genuine frame.',
    }
    receipt_path = output / 'native-render-receipt.json'
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0 if frame_info is not None else 1


if __name__ == '__main__':
    raise SystemExit(main())
