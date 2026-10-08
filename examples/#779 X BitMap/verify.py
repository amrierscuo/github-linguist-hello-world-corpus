from PIL import Image
with Image.open('hello.xbm') as im:
 im.load();assert im.format=='XBM' and im.size==(104,1)
 values=[im.getpixel((x,0))!=0 for x in range(104)]
 data=bytes(sum(int(values[i*8+b])<<b for b in range(8)) for i in range(13))
 assert data==b'Hello, World!'
 print(data.decode('ascii'));print('PASS: existing Pillow XBM image decoder and ASCII-packed pixel row')
