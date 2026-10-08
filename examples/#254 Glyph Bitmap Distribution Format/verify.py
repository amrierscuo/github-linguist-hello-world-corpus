from pathlib import Path
import json, sys, freetype
from PIL import Image
root = Path(__file__).parent
expected = json.loads((root/'glyphs.json').read_text(encoding='utf-8'))
font = freetype.Face(str(root/'hello.bdf'))
assert font.num_fixed_sizes == 1 and font.num_glyphs >= len(expected)
font.select_size(0)
image = Image.new('L', (len('Hello, World!')*6,7), 0)
for i, character in enumerate('Hello, World!'):
    assert font.get_char_index(ord(character)) != 0, repr(character)
    font.load_char(character, freetype.FT_LOAD_RENDER | freetype.FT_LOAD_TARGET_MONO)
    bitmap = font.glyph.bitmap
    assert bitmap.width == 5 and bitmap.rows == 7, (character, bitmap.width, bitmap.rows)
    rows = [''.join('1' if bitmap.buffer[row*bitmap.pitch+col//8] & (0x80>>(col%8)) else '0' for col in range(5)) for row in range(7)]
    assert rows == expected[character], (character,rows)
    for y,row in enumerate(rows):
        for x,bit in enumerate(row):
            if bit == '1': image.putpixel((i*6+x,y),255)
image.resize((image.width*8,image.height*8),Image.Resampling.NEAREST).save(sys.argv[1])
print('FreeType '+'.'.join(map(str,freetype.version()))+' original BDF load and every greeting glyph bitmap PASS.')
print('Hello, World!')
