from mako.template import Template
value = Template(filename="hello.mako").render(target="World")
assert value == "Hello, World!\n"
print(value, end="")
