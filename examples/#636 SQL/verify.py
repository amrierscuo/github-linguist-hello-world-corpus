from pathlib import Path
import sqlite3
with sqlite3.connect(":memory:") as db:
    actual, = db.execute(Path("hello.sql").read_text(encoding="utf8")).fetchone()
assert actual == "Hello, World!"
print(actual)
