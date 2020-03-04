from PIL import Image
import numpy as np
from colorama import Fore, Back, Style, init

#WIP, testing
def blur(rgb, blurLevel):
    print("Blur Time")
    if blurLevel == 0:
        rgb.show()
        return
    pixels = rgb.load()
    print("Size")
    print(rgb.size)
    new_size = (rgb.size[0]+blurLevel, rgb.size[1]+blurLevel)
    old_size = rgb.size

    temp_img = Image.new("RGB", new_size)
    temp_img.paste(rgb, (int((new_size[0]-old_size[0])/2),int((new_size[1]-old_size[1])/2)))
    tempPixels = temp_img.load()
    if blurLevel == 1:
        print("Blur 1")
        for x in range(rgb.size[0]):    # For every col
            for y in range(rgb.size[1]):    # For every row
                i = x + blurLevel
                j = y + blurLevel
                print(i-blurLevel)
                print(j-blurLevel)
                print(tempPixels[0,0])
                blurR = int((np.mean(tempPixels[i-blurLevel:i+blurLevel,j-blurLevel:j+blurLevel][0],dtype="float64")+np.mean(tempPixels[i-blurLevel:i+blurLevel, j][0],dtype="float64")+np.mean(tempPixels[i-blurLevel:i+blurLevel,j+blurLevel][0],dtype="float64"))/3)
                blurG = int((np.mean(tempPixels[i-blurLevel:i+blurLevel,j-blurLevel][1],dtype="float64")+np.mean(tempPixels[i-blurLevel:i+blurLevel, j][1],dtype="float64")+np.mean(tempPixels[i-blurLevel:i+blurLevel,j+blurLevel][1],dtype="float64"))/3)
                blurB = int((np.mean(tempPixels[i-blurLevel:i+blurLevel,j-blurLevel][2],dtype="float64")+np.mean(tempPixels[i-blurLevel:i+blurLevel, j][2],dtype="float64")+np.mean(tempPixels[i-blurLevel:i+blurLevel,j+blurLevel][2],dtype="float64"))/3)
                pixels[x, y] = (blurR, blurG, blurB)
    elif blurLevel == 2:
        print("Blur 2")
        for i in range(rgb.size[0]):    # For every col
            for j in range(rgb.size[1]):    # For every row
                blurR = int((np.mean(tempPixels[i-blurLevel:i+blurLevel, j-blurLevel][0])+np.mean(tempPixels[i-blurLevel:i+blurLevel, j][0])+np.mean(tempPixels[i-blurLevel:i+blurLevel,j+blurLevel][0]))/3)
                blurG = int((tempPixels[i, j-blurLevel][1]+tempPixels[i, j][1]+tempPixels[i, j+blurLevel][1]+tempPixels[i-blurLevel, j][1]+tempPixels[i+blurLevel, j][1]+tempPixels[i-blurLevel, j+blurLevel][1]+tempPixels[i+blurLevel, j-blurLevel][1]+tempPixels[i-blurLevel, j-blurLevel][1]+tempPixels[i+blurLevel, j+blurLevel][1])/9)
                blurB = int((tempPixels[i, j-blurLevel][2]+tempPixels[i, j][2]+tempPixels[i, j+blurLevel][2]+tempPixels[i-blurLevel, j][2]+tempPixels[i+blurLevel, j][2]+tempPixels[i-blurLevel, j+blurLevel][2]+tempPixels[i+blurLevel, j-blurLevel][2]+tempPixels[i-blurLevel, j-blurLevel][2]+tempPixels[i+blurLevel, j+blurLevel][2])/9)
                pixels[i, j] = (blurR, blurG, blurB)
    rgb.show()
