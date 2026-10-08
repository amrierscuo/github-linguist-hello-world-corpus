from pathlib import Path
import subprocess,os,time,shutil,json,sys
scratch=Path(sys.argv[1]);scratch.mkdir(parents=True,exist_ok=True)
for name in ['hello.bdf','fonts.alias']:shutil.copy2(name,scratch/name)
result=subprocess.run(['mkfontdir',str(scratch)],capture_output=True,text=True);print(json.dumps({'command':result.args,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr}))
assert result.returncode==0 and (scratch/'fonts.dir').read_text()==Path('fonts.dir').read_text()
display=':'+str(900+os.getpid()%100)
server=subprocess.Popen(['Xvfb',display,'-nolisten','tcp','-screen','0','100x100x24','-fp',str(scratch)+',/usr/share/fonts/X11/misc'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
try:
 query=None
 for _ in range(30):
  if server.poll() is not None:break
  time.sleep(.1)
  env=dict(os.environ,DISPLAY=display)
  query=subprocess.run(['xlsfonts','-ll','-fn','Hello, World!'],env=env,text=True,capture_output=True)
  if query.returncode==0 and 'Hello, World!' in query.stdout:break
 assert query is not None, 'Xvfb terminated before font query'
 print(json.dumps({'command':query.args,'exit_code':query.returncode,'stdout':query.stdout,'stderr':query.stderr}))
 assert query.returncode==0 and 'Hello, World!' in query.stdout
 print('PASS: authentic X font index generation and Xvfb font alias/property resolution')
finally:
 server.terminate();out,err=server.communicate(timeout=5);print(json.dumps({'xvfb_exit_code':server.returncode,'stdout':out,'stderr':err}))
