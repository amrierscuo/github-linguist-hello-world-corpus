from pathlib import Path
from pyfiglet import Figlet

font = str(Path("greeting").resolve())
renderer = Figlet(font=font, width=80)
assert renderer.Font.height == 1
output = renderer.renderText("Hello, World!")
assert output == "Hello, World!\n", repr(output)
print(output, end="")
