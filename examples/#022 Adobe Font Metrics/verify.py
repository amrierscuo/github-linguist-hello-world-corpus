from pathlib import Path
from fontTools.afmLib import AFM
import sys

font = AFM(sys.argv[1] if len(sys.argv) > 1 else 'hello.afm')
assert font.FontName == 'HelloCorpus'
assert font.FontBBox == (0, 0, 600, 700)
assert len(font.chars()) == 10
glyphs = ['H', 'e', 'l', 'l', 'o', 'comma', 'space', 'W', 'o', 'r', 'l', 'd', 'exclam']
codes = [font[g][0] for g in glyphs]
greeting = bytes(codes).decode('ascii')
assert greeting == 'Hello, World!'
width = sum(font[g][1] for g in glyphs)
assert width == 7500
assert font['space'] == (32, 300, (0, 0, 0, 0))
print(greeting)
print(f'PASS: 10 glyph metrics; total advance = {width} units; FontBBox = {font.FontBBox}')
