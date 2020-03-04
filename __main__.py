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
from scale import scale

def main():
    init(autoreset=True)
    print(Fore.CYAN + '-'*30)
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:x:w:y:", ["help","image=", "output=", "intensity=","width=","height="])
    output = False
    imgURL = ""
    outputFile = ""
    w=""
    h=""
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
            print("Blur Arg: " + arg)
            print(int(arg))
            if blurLevel != 0 and blurLevel != 2 and blurLevel != 1:
                blurLevel = 0
        elif opt in ("-w", "--width"):
            w = int(arg)
        elif opt in ("-y", "--height"):
            h = int(arg)

    #Open and show original
    try:
        im = Image.open(imgURL)
        im.show()
    except:
        print(Fore.RED + "Invalid Filepath or File Type")
    #Check for processing method
    if(args[0] == "rgb2gray" or args[0] == "rgb2grey"):
        rgb2gray(im)
    elif(args[0] == "blur"):
        print("Blur Level: " + str(blurLevel))
        blur(im,blurLevel)
    elif(args[0] == "scale"):
        scale(im,int(w),int(h))
    #Save if user wants to
    if output:
        im.save(outputFile)
                
            
    print(Fore.CYAN + '-'*30)

if __name__ == '__main__':
    main()