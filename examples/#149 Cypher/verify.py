from pathlib import Path
import kuzu
print("Kuzu", kuzu.__version__)
db = kuzu.Database("db", buffer_pool_size=64*1024*1024, max_num_threads=1)
conn = kuzu.Connection(db)
result = conn.execute(Path("hello.cypher").read_text(encoding="utf-8"))
assert result.get_column_names() == ["greeting"]
assert result.get_next() == ["Hello, World!"]
assert not result.has_next()
print("PASS: one row, greeting = Hello, World!")
conn.close()
db.close()
