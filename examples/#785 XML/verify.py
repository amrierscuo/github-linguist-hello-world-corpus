from lxml import etree
parser = etree.XMLParser(no_network=True, resolve_entities=False)
root = etree.parse("hello.xml", parser).getroot()
assert root.tag == "greeting" and root.get("audience") == "World"
assert root.text == "Hello, World!"
print(root.text)
