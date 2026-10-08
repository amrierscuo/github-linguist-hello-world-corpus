from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import os
import subprocess
import threading

class GreetingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        assert self.path == "/greeting"
        body = b"Hello, World!"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", 0), GreetingHandler)
thread = threading.Thread(target=server.serve_forever)
thread.start()
try:
    executable = os.environ.get("HURL_BINARY", "hurl")
    result = subprocess.run([executable, "--test", "--variable", f"port={server.server_port}", "--noproxy", "*", "hello.hurl"], capture_output=True, text=True, timeout=15)
    print(result.stdout, end="")
    print(result.stderr, end="")
    if result.returncode:
        raise RuntimeError(f"Hurl exited with {result.returncode}")
finally:
    server.shutdown()
    server.server_close()
    thread.join(timeout=5)
    assert not thread.is_alive()
    print("CLEANUP: loopback HTTP fixture stopped and socket closed")
