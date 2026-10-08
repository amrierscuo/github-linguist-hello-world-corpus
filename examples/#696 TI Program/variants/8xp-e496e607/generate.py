from pathlib import Path
from importlib.metadata import version
from tivars.types import TIProgram
from tivars.models import TI_84P
print("tivars", version("tivars"))
source = Path("greeting.txt").read_text().strip()
program = TIProgram(name="HELLO")
program.load_string(source)
program.export(model=TI_84P).save("hello.8xp")
loaded = TIProgram.open("hello.8xp")
assert loaded.string() == source
assert loaded.bytes() == program.bytes()
print("TI-84 Plus tokenized program roundtrip:", loaded.string())
