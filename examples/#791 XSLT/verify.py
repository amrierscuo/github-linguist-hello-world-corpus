from lxml import etree
parser = etree.XMLParser(no_network=True, resolve_entities=False)
transform = etree.XSLT(etree.parse("hello.xsl", parser))
actual = str(transform(etree.parse("input.xml", parser)))
assert actual == "Hello, World!"
print(actual)
