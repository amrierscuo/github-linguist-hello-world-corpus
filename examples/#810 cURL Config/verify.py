from pathlib import Path
from http.server import BaseHTTPRequestHandler,HTTPServer
import threading,subprocess,json,sys
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  text=self.headers.get("X-Corpus-Greeting","")
  self.send_response(200);self.send_header("Content-Type","text/plain");self.end_headers();self.wfile.write(text.encode())
 def log_message(self,*args):pass
server=HTTPServer(("127.0.0.1",0),Handler)
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
try:
 r=subprocess.run([sys.argv[1],"--disable","--config",".curlrc",f"http://127.0.0.1:{server.server_port}/"],capture_output=True,text=True)
 assert r.returncode==0 and r.stdout=="Hello, World!",(r.returncode,r.stdout,r.stderr)
 print(json.dumps({"command":"curl --disable --config .curlrc <loopback-url>","exit_code":r.returncode,"stdout":r.stdout,"stderr":r.stderr}))
finally:server.shutdown();server.server_close();thread.join()
