import io,pickle,pickletools,sys
from pathlib import Path
class DataOnly(pickle.Unpickler):
    def find_class(self,module,name):raise pickle.UnpicklingError('Globals are disallowed')
data=Path('hello.pkl').read_bytes()
pickletools.dis(data)
value=DataOnly(io.BytesIO(data)).load()
assert value=={'message':'Hello, World!','language':'en'}
print(value['message'])
print('PASS: genuine Pickle disassembler and restricted native data loader')
