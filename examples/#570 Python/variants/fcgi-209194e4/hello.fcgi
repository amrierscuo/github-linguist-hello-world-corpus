#!/usr/bin/env python3
from flup.server.fcgi import WSGIServer
def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain; charset=utf-8")])
    return [b"Hello, World!\n"]
if __name__ == "__main__":
    WSGIServer(application).run()
