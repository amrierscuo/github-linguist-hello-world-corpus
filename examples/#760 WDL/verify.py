import WDL
doc = WDL.load("hello.wdl")
assert doc.workflow.name == "greeting"
assert len(doc.tasks) == 1 and doc.tasks[0].name == "hello"
print("PASS: original WDL parser and typechecker")
