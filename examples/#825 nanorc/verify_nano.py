import os,pty,fcntl,termios,struct,subprocess,time,select,json,sys
master,slave=pty.openpty()
fcntl.ioctl(slave,termios.TIOCSWINSZ,struct.pack("HHHH",24,90,0,0))
env=dict(os.environ,TERM="xterm-256color")
process=subprocess.Popen([sys.argv[1],"--rcfile","hello.nanorc","greeting.hello"],stdin=slave,stdout=slave,stderr=slave,env=env)
os.close(slave)
data=b"";deadline=time.monotonic()+4
while time.monotonic()<deadline:
 if select.select([master],[],[],0.15)[0]:
  try:data+=os.read(master,65536)
  except OSError:break
 if b"Hello, World!" in data:break
os.write(master,b"\x18")
deadline=time.monotonic()+3
while time.monotonic()<deadline and process.poll() is None:
 if select.select([master],[],[],0.1)[0]:
  try:data+=os.read(master,65536)
  except OSError:break
if process.poll() is None:process.terminate()
code=process.wait(timeout=3);os.close(master)
screen=data.decode("utf8",errors="replace")
assert code==0 and "Hello, World!" in screen and "Error in" not in screen,(code,screen)
assert "\x1b[34mHello, World!" in screen and "\x1b[0;1m" in screen,screen
print(json.dumps({"command":"nano --rcfile hello.nanorc greeting.hello (real PTY; Ctrl-X)","exit_code":code,"stdout":screen,"stderr":""}))
