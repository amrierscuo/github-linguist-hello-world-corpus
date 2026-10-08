from pathlib import Path
import subprocess, os, time, urllib.request, socket
binary = os.environ.get('NGINX_BINARY', 'nginx')
prefix = str(Path.cwd()) + '/'
args = [binary, '-p', prefix, '-c', str(Path('hello.vhost').resolve()), '-e', str(Path('error.log').resolve())]
check = subprocess.run(args + ['-t'], capture_output=True, text=True)
print(check.stdout, end='')
print(check.stderr, end='')
assert check.returncode == 0, 'nginx rejected configuration'
server = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
try:
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    for attempt in range(30):
        try:
            with opener.open('http://127.0.0.1:18080/greeting', timeout=1) as response:
                assert response.status == 200
                body = response.read()
            break
        except OSError:
            if server.poll() is not None: raise RuntimeError('nginx terminated early')
            time.sleep(0.1)
    else: raise RuntimeError('nginx did not start')
    assert body == b'Hello, World!'
    print(body.decode('ascii'))
finally:
    server.terminate()
    try: output, errors = server.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        server.kill()
        output, errors = server.communicate(timeout=5)
    print(output, end='')
    print(errors, end='')
    assert server.poll() is not None
    with socket.socket() as probe:
        probe.settimeout(1)
        assert probe.connect_ex(('127.0.0.1', 18080)) != 0
    print('CLEANUP: dedicated nginx process stopped; loopback listener closed.')
