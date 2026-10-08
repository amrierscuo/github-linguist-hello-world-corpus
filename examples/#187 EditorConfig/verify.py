from pathlib import Path
import editorconfig

file = Path("greeting.txt").resolve()
properties = editorconfig.get_properties(str(file))
for key, expected in {"charset": "utf-8", "end_of_line": "lf", "insert_final_newline": "true", "indent_style": "space", "indent_size": "2"}.items():
    assert properties[key] == expected, (key, properties)
assert file.read_bytes() == b"Hello, World!\n"
print("EditorConfig resolved greeting.txt: UTF-8, LF, final newline, 2 spaces")
