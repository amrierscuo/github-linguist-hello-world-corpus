import orgparse
root = orgparse.load("hello.org")
assert len(root.children) == 1
assert root.children[0].heading == "Hello, World!"
print(root.children[0].heading)
