from fontTools.ttLib import TTFont
from fontTools.feaLib.builder import addOpenTypeFeatures
font = TTFont()
font.setGlyphOrder([".notdef"])
addOpenTypeFeatures(font, "hello.fea")
values = [entry.toUnicode() for entry in font["name"].names if entry.nameID == 4]
assert values and all(value == "Hello, World!" for value in values)
print(values[0])
