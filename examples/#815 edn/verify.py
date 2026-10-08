from edn_format import loads,Keyword
from pathlib import Path
data=loads(Path("hello.edn").read_text())
assert data[Keyword("greeting")]=="Hello, World!"
assert data[Keyword("language")]==Keyword("edn")
print(data[Keyword("greeting")])
