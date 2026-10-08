import plistlib
with open("hello.plist", "rb") as stream: data = plistlib.load(stream)
assert data == {"greeting": "Hello, World!"}
print(data["greeting"])
