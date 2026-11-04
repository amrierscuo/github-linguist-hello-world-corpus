from pathlib import Path
import sqlite3,sys
source=Path(sys.argv[1]).read_text(encoding="utf8")
with sqlite3.connect(":memory:") as db:
    results=[]
    statement=""
    for line in source.splitlines(keepends=True):
        statement+=line
        if sqlite3.complete_statement(statement):
            cursor=db.execute(statement)
            if cursor.description:
                results.append(cursor.fetchall())
            statement=""
    assert not statement.strip(), repr(statement)
    assert results==[[("Hello, World!",)]], results
print(results[0][0][0])
