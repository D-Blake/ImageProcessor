from PIL import Image
import numpy as np
from colorama import Fore, Back, Style, init


def blur(rgb, blurLevel):
    if blurLevel == 0:
        rgb.show()
        return
    pixels = rgb.load()
    new_size = (rgb[0]+blurLevel, rgb[1]+blurLevel)
    old_size = rgb.size

    temp_img = Image.new("RGB", new_size)
    temp_img.paste(rgb, ((new_size[0]-old_size[0])/2,(new_size[1]-old_size[1])/2))
    for i in range(rgb.size[0]):    # For every col
            for j in range(rgb.size[1]):    # For every row
                blurR = int((pixels[i, j-blurLevel][0]+pixels[i, j][0]+pixels[i, j+blurLevel][0])/3)
                blurG = int((pixels[i, j-blurLevel][1]+pixels[i, j][1]+pixels[i, j+blurLevel][1])/3)
                blurB = int((pixels[i, j-blurLevel][2]+pixels[i, j][2]+pixels[i, j+blurLevel][2])/3)
                pixels[i, j] = (blurR, blurG, blurB)
    rgb.show()
