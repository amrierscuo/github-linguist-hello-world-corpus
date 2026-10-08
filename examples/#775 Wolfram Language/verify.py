from pathlib import Path
from mathics.core.load_builtin import import_and_load_builtins
from mathics.session import MathicsSession
import_and_load_builtins()
session=MathicsSession()
session.evaluate(Path('hello.wl').read_text())
outputs=[str(item.text) for item in session.evaluation.out]
assert outputs==['Hello, World!'],outputs
print(outputs[0])
print('PASS: genuine Mathics3 Wolfram Language evaluator runs StringJoin and Print')
