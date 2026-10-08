from pathlib import Path
actual = Path("hello.txt").read_text(encoding="utf8")
assert actual == "Hello, World!\n"
print(actual, end="")
