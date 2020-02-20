from PIL import Image
import numpy as np 
from colorama import Fore, Back, Style, init

def rgb2gray(rgb):
    pixels = rgb.load()
    for i in range(rgb.size[0]):    # For every col
        for j in range(rgb.size[1]):    # For every row
            gray = int((pixels[i,j][0]+pixels[i,j][1]+pixels[i,j][2])/3)
            pixels[i,j] = (gray, gray, gray)
    rgb.show()
