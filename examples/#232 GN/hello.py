from pathlib import Path
import sys
greeting = "Hello, " + "World!"
output = Path(sys.argv[1])
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(greeting + "\n", encoding="utf-8", newline="\n")
print(greeting)
