import sys
from pypdf import PdfReader
text="".join(p.extract_text() for p in PdfReader(sys.argv[1]).pages)
assert text.strip()=="Hello, World!",repr(text)
print(text.strip())
