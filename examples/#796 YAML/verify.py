from pathlib import Path
import yaml
data = yaml.safe_load(Path("hello.yml").read_text(encoding="utf8"))
assert data == {"greeting": "Hello, World!"}
print(data["greeting"])
