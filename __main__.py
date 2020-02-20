"""
This exercise should allow the following:

1- Blur Filter must be in its own module and called through your cli with
    'python3 ImageProcessor -i someimage -o someoutputimage -x somenumber blur'
3- Add option -x to tell your blur algorithm how "intense" to do the blur you 
    can decide what the range of this value is, e.g. 0-100 as in 0% blur to 100% blur
4- Add option to your cli to write the blurred image to a given output, -o/--output
5- Raise errors where appropriate
"""
from PIL import Image
import numpy as np 
import getopt, sys
from colorama import Fore, Back, Style, init
from greyscale import rgb2gray
from blur import blur

def main():
    init(autoreset=True)
    print(Fore.CYAN + '-'*30)
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:x:", ["help","image=", "output=", "intensity="])
    output = False
    imgURL = ""
    outputFile = ""
    blurLevel = 0
    #Debugging Lines
    print(opts)
    print(args)
    #Check for if they want image info, image processing, and/or image saving
    for opt, arg in opts:
        if opt in ("-h","--help"):
            #run help
            print(Fore.GREEN + "Please input the image filepath")
        elif opt in ("-i", "--image"):
            try:
                imgURL = arg
                im = Image.open(imgURL)
                if(len(opts)<2):
                    print(Fore.GREEN + "Image Opened")
                    print(Fore.GREEN + "Resolution: " + str(im.size))
                    print(Fore.GREEN + "Mode: " + str(im.mode))
                    print(Fore.GREEN + "Filename: " + str(im.filename))
            except:
                print(Fore.RED + "Invalid Filepath or File Type")
                break
        elif opt in ("-o", "--output"):
            output = True
            outputFile = arg
        elif opt in ("-x", "--intensity"):
            blurLevel = int(arg)
            if blurLevel is not 0 or blurLevel is not 2 or blurLevel is not 1:
                blurLevel = 0

    #Open and show original
    im = Image.open(imgURL)
    im.show()
    #Check for processing method
    if(args[0] == "rgb2gray" or arg[0] == "rgb2grey"):
        rgb2gray(im)
    elif(arg[0] == "blur"):
        blur(im,blurLevel)
    #Save if user wants to
    if output:
        im.save(outputFile)
                
            
    print(Fore.CYAN + '-'*30)

if __name__ == '__main__':
    main()