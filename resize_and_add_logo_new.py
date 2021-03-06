#! /usr/bin/env python3
# resize_and_add_logo.py - Resizes all images in current working directory to
# fit in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image


SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'


os.makedirs('with_logo', exist_ok=True)

# Loop over all files in the working directory.
for filename in os.listdir('.'):
    logo_im = Image.open(LOGO_FILENAME)
    logo_width, logo_height = logo_im.size
    if not filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename  == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself
    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:

        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

        logo_width = logo_height = int((SQUARE_FIT_SIZE / 10))
        logo_im = logo_im.resize((logo_width, logo_height))

        # Add the logo.
        print('Adding logo to %s...' % (filename))
        im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)

        # Save changes.
        im.save(os.path.join('./with_logo', filename))
