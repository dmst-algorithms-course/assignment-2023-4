from PIL import Image
import sys

def text_to_image(filename):
    with open(filename, 'r') as f:
        lines = [line.strip().split() for line in f]

    width = len(lines[0])
    height = len(lines)
    img = Image.new('1', (width, height))

    for y, line in enumerate(lines):
        for x, pixel in enumerate(line):
            # Invert pixel value, as 1 is black in the image.
            if pixel == '1':
                img.putpixel((x, y), 0)
            else:
                img.putpixel((x, y), 1)

    return img

img = text_to_image(sys.argv[1])
img.show()
