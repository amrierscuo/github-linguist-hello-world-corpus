from pathlib import Path
import socket
import threading
import h11

wire_response = Path("hello.http").read_bytes()
errors = []
listener = socket.socket()
listener.bind(("127.0.0.1", 0))
listener.listen(1)
listener.settimeout(5)
port = listener.getsockname()[1]

def serve():
    try:
        with listener.accept()[0] as peer:
            peer.settimeout(5)
            server = h11.Connection(h11.SERVER)
            server.receive_data(peer.recv(4096))
            request = server.next_event()
            assert isinstance(request, h11.Request) and request.target == b"/greeting"
            peer.sendall(wire_response)
    except BaseException as error:
        errors.append(error)

thread = threading.Thread(target=serve)
thread.start()
try:
    client = h11.Connection(h11.CLIENT)
    with socket.create_connection(("127.0.0.1", port), timeout=5) as peer:
        peer.sendall(client.send(h11.Request(method="GET", target="/greeting", headers=[("Host", "localhost")])) + client.send(h11.EndOfMessage()))
        chunks = []
        while True:
            chunk = peer.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)
    client.receive_data(b"".join(chunks))
    response = client.next_event()
    assert isinstance(response, h11.Response) and response.status_code == 200
    body = bytearray()
    while True:
        event = client.next_event()
        if isinstance(event, h11.Data):
            body.extend(event.data)
        elif isinstance(event, h11.EndOfMessage):
            break
        else:
            raise AssertionError(event)
    assert bytes(body) == b"Hello, World!"
    print("PASS: h11 parsed HTTP 200 body = Hello, World!")
finally:
    listener.close()
    thread.join(timeout=6)
    assert not thread.is_alive(), "Loopback fixture did not stop"
    print("CLEANUP: listener closed; fixture thread stopped")
if errors:
    raise errors[0]
