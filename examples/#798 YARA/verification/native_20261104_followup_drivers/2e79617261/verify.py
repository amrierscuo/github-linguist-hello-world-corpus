import yara
rules = yara.compile(filepath="hello.yara")
assert [x.rule for x in rules.match(data=b"Hello, World!")] == ["CorpusGreeting"]
assert rules.match(data=b"Hello, Moon!") == []
print("Hello, World!")
