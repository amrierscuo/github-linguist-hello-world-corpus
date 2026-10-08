from pathlib import Path
import clingo

control = clingo.Control(["0"])
control.load(str(Path(__file__).with_name("hello.lp")))
control.ground([("base", [])])
models = []
with control.solve(yield_=True) as handle:
    for model in handle:
        models.append([str(symbol) for symbol in model.symbols(shown=True)])
    result = handle.get()
assert result.satisfiable and result.exhausted, str(result)
assert models == [['greeting("Hello, World!")']], models
print("Hello, World!")
print("Verified: exactly one answer set with the expected greeting atom.")
