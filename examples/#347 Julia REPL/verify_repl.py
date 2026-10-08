from pathlib import Path
import json,os,queue,re,subprocess,sys,threading,time
from winpty import PtyProcess

exe=Path(sys.argv[1]).resolve();scratch=Path(sys.argv[2]).resolve()
env=dict(os.environ,TERM='dumb',JULIA_DEPOT_PATH=str(scratch/'depot'))
command=[str(exe),'--startup-file=no','--history-file=no','--color=no','--banner=no']
process=PtyProcess.spawn(subprocess.list2cmdline(command),env=env,dimensions=(30,160))
messages=queue.Queue();pieces=[]
def reader():
    try:
        while True: messages.put(process.read())
    except EOFError: messages.put(None)
threading.Thread(target=reader,daemon=True).start()
def wait_prompt():
    deadline=time.monotonic()+20;chunk=''
    while time.monotonic()<deadline:
        try: item=messages.get(timeout=.2)
        except queue.Empty: continue
        if item is None: raise RuntimeError('REPL exited before prompt')
        pieces.append(item);chunk+=item
        if 'julia>' in chunk: return
    raise TimeoutError('No native REPL prompt: '+chunk)
inputs=Path('repl-input.txt').read_text(encoding='utf-8').splitlines()
try:
    wait_prompt()
    for line in inputs[:-1]:
        process.write(line+'\r');wait_prompt()
    assert inputs[-1]=='exit()'
    process.write(inputs[-1]+'\r');process.wait()
    time.sleep(.1)
    while not messages.empty():
        item=messages.get()
        if item: pieces.append(item)
    raw=''.join(pieces)
    cleaned=re.sub(r'\x1b\[[0-?]*[ -/]*[@-~]', '', raw).replace('\r\n','\n')
    transcript=cleaned[cleaned.index('julia>'):]
    transcript=re.sub(r'\n{3,}','\n\n',transcript)
    assert process.exitstatus==0
    assert 'ERROR:' not in transcript
    assert 'julia> name = "World"\n' in transcript
    assert '\n"World"\n' in transcript
    assert 'julia> println("Hello, ", name, "!")\n' in transcript
    assert '\nHello, World!\n' in transcript
    (scratch/'capture.json').write_text(json.dumps({'command':command,'stdin_lines':inputs,'exit_code':process.exitstatus,'raw_terminal_output':raw,'transcript':transcript},indent=2),encoding='utf-8')
    (scratch/'transcript.txt').write_text(transcript,encoding='utf-8',newline='\n')
    print(json.dumps({'exit_code':process.exitstatus,'raw_terminal_output':raw,'transcript':transcript}))
    print('PASS: genuine native Julia terminal REPL, prompts, value display and greeting')
finally:
    if process.isalive(): process.terminate(force=True)
