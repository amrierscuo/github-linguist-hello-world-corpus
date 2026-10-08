from pathlib import Path
import sqlglot
query = sqlglot.parse_one(Path("hello.hql").read_text(), read="hive")
print(query.sql(dialect="hive"))
