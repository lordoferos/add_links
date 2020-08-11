#! python3
# photolinks.py - Resizes images and adds website link to lower right corner

import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

SQUARE_FIT_SIZE = 600

link = 'www.dailyupdates.co.ke'


# Loop over all files in the working directory.
os.makedirs('withlink', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.JPG')):
        continue # skip non-image files 

    im = Image.open(filename)
    width, height = im.size


    # Check if the image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE /width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE /height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

        # Add the link top left
        print('Adding link to %s...' % (filename))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("sans-serif.ttf", 16)
        draw.text((0,0), link, (0,0,0), font=font)
        
        
        # Save changes
        im.save(os.path.join('withlink', filename + '_link.jpg'))