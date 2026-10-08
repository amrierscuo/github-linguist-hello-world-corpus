from gedcom.parser import Parser
from pathlib import Path
parser = Parser()
parser.parse_file(str(Path("hello.ged")), strict=True)
notes = [item for item in parser.get_root_child_elements() if item.get_tag() == "NOTE"]
assert len(notes) == 1 and notes[0].get_value() == "Hello, World!"
print("PASS: GEDCOM NOTE = Hello, World!")
