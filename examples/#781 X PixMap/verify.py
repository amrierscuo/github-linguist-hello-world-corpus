from PIL import Image
image = Image.open("hello.xpm"); image.load()
assert image.size == (82, 9) and image.format == "XPM"
image.convert("RGB").resize((984, 108), Image.Resampling.NEAREST).save("preview.png")
print("Original XPM decoder: 82x9 pixels, preview.png produced")
