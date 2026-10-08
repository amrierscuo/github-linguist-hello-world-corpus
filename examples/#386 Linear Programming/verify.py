from pathlib import Path
import sys
text=Path(sys.argv[1]).read_text(encoding='utf-8')
assert 'c Status:     OPTIMAL' in text, text
columns={}
for line in text.splitlines():
 fields=line.split()
 if fields and fields[0]=='j': columns[int(fields[1])]=float(fields[3])
assert set(columns)==set(range(1,14)),columns
values=[columns[i] for i in range(1,14)]
assert all(v.is_integer() for v in values)
greeting=''.join(chr(int(v)) for v in values)
assert greeting=='Hello, World!',greeting
print(greeting)
