from pathlib import Path
from hyperon import MeTTa
source = Path("hello.metta").read_text(encoding="utf-8")
MeTTa().run(source)
