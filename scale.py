from PIL import Image
import numpy as np 
from colorama import Fore, Back, Style, init

def scale(rgb,w,h):
    pixels = rgb.load()
    target = Image.new("RGB", (w,h))
    width = rgb.size[0]
    height = rgb.size[1]
    temp = target.load()
    for x in range(0, w):  
      for y in range(0, h):
        srcX = int( round( float(x) / float(w) * float(width) ) )
        srcY = int( round( float(y) / float(h) * float(height) ) )
        srcX = min( srcX, width-1)
        srcY = min( srcY, height-1)
        temp[x,y] = (pixels[srcX,srcY][0],pixels[srcX,srcY][1],pixels[srcX,srcY][2])

    target.show()