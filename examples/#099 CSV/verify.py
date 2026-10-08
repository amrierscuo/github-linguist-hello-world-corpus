from pathlib import Path
import csv
import io

with open('hello.csv', encoding='utf-8', newline='') as handle:
    rows = list(csv.reader(handle, dialect='excel', strict=True))
assert rows == [['greeting'], ['Hello, World!']], rows
out = io.StringIO(newline='')
csv.writer(out, dialect='excel', lineterminator='\r\n').writerows(rows)
assert out.getvalue().encode('utf-8') == Path('hello.csv').read_bytes()
print(rows[1][0])
print('Python csv strict parsing and RFC 4180-style CRLF roundtrip PASS.')
