from oso import Oso, Variable
engine = Oso()
engine.load_files(['hello.polar'])
solutions = list(engine.query_rule('greeting', Variable('message')))
assert len(solutions) == 1
actual = solutions[0]['bindings']['message']
assert actual == 'Hello, World!'
print(actual)
