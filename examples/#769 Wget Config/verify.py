from pathlib import Path
import http.server,threading,subprocess,os,json
observed=[]
class Greeting(http.server.BaseHTTPRequestHandler):
 def do_GET(self):
  observed.append(self.headers.get('User-Agent'));body=Path('hello.txt').read_bytes();self.send_response(200);self.end_headers();self.wfile.write(body)
 def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Greeting)
worker=threading.Thread(target=server.serve_forever,daemon=True);worker.start()
try:
 env=dict(os.environ,WGETRC=str(Path('.wgetrc').resolve()))
 result=subprocess.run(['wget','--quiet','--output-document=-','http://127.0.0.1:'+str(server.server_port)+'/hello.txt'],env=env,text=True,capture_output=True,timeout=10)
 print(json.dumps({'command':result.args,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'observed_user_agent':observed},ensure_ascii=False))
 assert result.returncode==0 and result.stdout=='Hello, World!\n' and observed==['Hello, World!']
 print('PASS: native GNU Wget reads config and sends exact User-Agent to loopback server')
finally:server.shutdown();server.server_close();worker.join()
