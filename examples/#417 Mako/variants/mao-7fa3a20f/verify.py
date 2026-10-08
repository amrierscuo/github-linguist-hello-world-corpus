from mako.template import Template
value = Template(filename="hello.mao").render(target="World")
assert value == "Hello, World!\n"
print(value, end="")
