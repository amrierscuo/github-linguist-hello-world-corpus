from pathlib import Path
import vdf
value = vdf.loads(Path("hello.vdf").read_text(encoding="utf-8"))
assert value == {"Greeting": {"message": "Hello, World!"}}
print(value["Greeting"]["message"])
