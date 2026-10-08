from pathlib import Path
import subprocess,sys,time,urllib.request

prefix = Path(sys.argv[1]).resolve()
config = Path(sys.argv[2]).resolve()
exe = prefix / 'usr/sbin/haproxy'
import os
env = dict(os.environ, LD_LIBRARY_PATH=str(prefix/'usr/lib/x86_64-linux-gnu'))
process = subprocess.Popen([str(exe), '-db', '-f', str(config)], env=env,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
try:
    response = None
    for _ in range(50):
        if process.poll() is not None: raise RuntimeError(process.communicate())
        try:
            response = urllib.request.urlopen('http://127.0.0.1:18881/', timeout=1)
            break
        except OSError: time.sleep(.1)
    assert response is not None
    with response:
        assert response.status == 200
        assert response.headers['Content-Type'] == 'text/plain'
        body = response.read().decode('utf-8')
        assert body == 'Hello, World!', body
    print(body)
    print('PASS: genuine HAProxy localhost HTTP response')
finally:
    process.terminate()
    try: out, err = process.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill(); out, err = process.communicate()
    if out: print(out, end='')
    if err: print(err, end='', file=sys.stderr)
