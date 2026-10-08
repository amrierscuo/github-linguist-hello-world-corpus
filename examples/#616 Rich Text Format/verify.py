from pathlib import Path
from striprtf.striprtf import rtf_to_text
text=rtf_to_text(Path('hello.rtf').read_text(encoding='ascii'))
assert text.strip()=='Hello, World!'
print(text.strip())
print('PASS: existing striprtf parser decodes the RTF body')
