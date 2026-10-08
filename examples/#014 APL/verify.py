"""Run the authentic dzaima/APL interpreter and check output."""
import argparse
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--jar', required=True)
args = parser.parse_args()
source = Path(__file__).with_name('hello.apl')
result = subprocess.run(['java', '-jar', args.jar, '-f', str(source)],
                        capture_output=True)
if result.returncode != 0 or result.stderr or result.stdout not in (b'Hello, World!\n', b'Hello, World!\r\n'):
    raise SystemExit(f'FAIL exit={result.returncode}, stdout={result.stdout!r}, stderr={result.stderr!r}')
print('dzaima/APL interpreter: exit 0, stderr empty')
print('stdout bytes:', repr(result.stdout))
print('stdout matches exact greeting and one line ending (LF or CRLF)')
