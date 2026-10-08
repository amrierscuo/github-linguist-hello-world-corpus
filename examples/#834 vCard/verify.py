from pathlib import Path
import vobject
source=Path("hello.vcf").read_bytes()
assert b"\r\n" in source and b"\n" not in source.replace(b"\r\n",b"")
v=vobject.readOne(source.decode())
assert v.fn.value=="Hello, World!"
assert v.email.value=="hello@example.invalid"
again=vobject.readOne(v.serialize())
assert again.fn.value=="Hello, World!"
print(v.fn.value)
