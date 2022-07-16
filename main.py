from PIL import Image
import sys

def Convert(image):
    imagename = image.split('.')[0]
    im = Image.open(image)
    im.save(f'{imagename}.png')

for x in sys.argv:
    try:
        Convert(x)
    except:
        pass
