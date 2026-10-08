from pathlib import Path
import importlib.metadata, sys
from pygerber.gerberx3.api.v2 import GerberFile, OnParserErrorEnum
from PIL import Image
parsed = GerberFile.from_file(Path(__file__).with_name('hello.gbr')).parse(on_parser_error=OnParserErrorEnum.Raise)
parsed.render_raster(sys.argv[1], dpmm=80)
image = Image.open(sys.argv[1])
assert image.width > 10 * image.height, image.size
assert len(image.getcolors(maxcolors=65536)) > 1
print('PyGerber '+importlib.metadata.version('pygerber')+' tokenizer/parser/renderer PASS.')
print('Rendered original Hello, World! dot vectors:', image.size)
