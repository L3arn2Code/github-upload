from PIL import Image
import sys, os

path = sys.argv[1]

fn, fext = os.path.splitext(path)

im = Image.open(path)
width, height = im.size

for w in range(width):
    for h in range(height):
            r, g, b = im.getpixel((w,h))
            if r>150:
                    im.putpixel((w,h), (255,255,255))

im.save(f'{fn}-white-bg.jpg')
im.save(f'{fn}-white-bg.png')