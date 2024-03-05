from PIL import Image

import ST7735

from DebugConsoleLogger import debug_log


def wellcome_message(disp, path):
    image_file = path

    WIDTH = disp.width
    HEIGHT = disp.height

    # Load an image.
    debug_log('Loading image: {}...'.format(image_file))
    image = Image.open(image_file)

    # Resize the image
    image = image.resize((WIDTH, HEIGHT))
    B, G, R = image.split()[0:3]
    image = Image.merge("RGB", (R, G, B))
    # Draw the image on the display hardware.
    debug_log('Drawing image')

    disp.display(image)
