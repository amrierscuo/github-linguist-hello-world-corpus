import gemmi
block = gemmi.cif.read_file("hello.star").sole_block()
actual = gemmi.cif.as_string(block.find_value("_greeting"))
assert actual == "Hello, World!"
print(actual)
