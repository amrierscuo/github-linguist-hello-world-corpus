from pathlib import Path
import sys
from pykickstart.parser import KickstartParser
from pykickstart.version import makeVersion
handler=makeVersion('F42');parser=KickstartParser(handler)
parser.readKickstart(str(Path(sys.argv[1]).resolve()))
assert handler.lang.lang=='en_US.UTF-8'
assert handler.timezone.timezone=='UTC'
assert len(handler.scripts)==1
script=handler.scripts[0]
assert not script.inChroot
assert script.script.strip()=="printf '%s\\n' 'Hello, World!'"
print('PASS: authentic Pykickstart F42 parser; post-script preserved as data, never executed')
