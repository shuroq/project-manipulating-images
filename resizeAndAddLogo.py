import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'

logoIm = Image.open( LOGO_FILENAME )
logoWidth, logoHeight = logoIm.size

#TODO: Loop over all files in the working directory
#TODO: Check if file image needs to be
#TODO: Calculate the new width and height to resize to.
#TODO: Add the logo.
#TODO: Save changes.
import os
from PIL import Image

SQUARE_FIT_SIZE = 300
height = 300
width = 300

LOGO_FILENAME = 'logo.png'
logoIm = Image.open( LOGO_FILENAME )
logoWidth, logoHeight = logoIm.size

#I used exception because I use Python 2.7; the argument exist_ok=True only works with python 3.0+
try:
    os.makedirs('withLogo')
except OSError:
    pass

for image in os.listdir('.'):
    if not (image.endswith('.png') or image.endswith('.jpg')) \
        or image == LOGO_FILENAME:
        continue
    im = Image.open(image)
    #width, height = im.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)

    else:
        width = int((SQUARE_FIT_SIZE / height) * width)
        height = SQUARE_FIT_SIZE

    print ('Resizing %s...' % (image))
    im = im.resize((width, height))
    print('Adding logo to %s...' % (image))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(os.path.join('withLogo', image))
