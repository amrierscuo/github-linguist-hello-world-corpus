from pathlib import Path
import io,sys
sys.path.insert(0,str(Path(sys.argv[1]).resolve()))
from greeting import Greeting
from kaitaistruct import KaitaiStream,ValidationNotEqualError
data=Path(sys.argv[2]).read_bytes();parsed=Greeting(KaitaiStream(io.BytesIO(data)))
assert parsed.magic==b'HW' and parsed.length==13 and parsed.message=='Hello, World!'
assert parsed._io.pos()==len(data)
try: Greeting(KaitaiStream(io.BytesIO(b'XX'+data[2:])))
except ValidationNotEqualError: pass
else: raise AssertionError('Incorrect magic accepted')
print(parsed.message)
print('PASS: genuinely generated Kaitai parser, original binary fixture and magic control')
