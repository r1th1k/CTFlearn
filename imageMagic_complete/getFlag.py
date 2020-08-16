#!/usr/bin/env python3

from PIL import Image
import subprocess

#storing an image in img object
img = Image.open('out copy.jpg')

#if you want you can uncommet it to get the size of the original image to find the original height
#width,height = img.size
#print(width,height)

#loading the data in a variable for working
imgdat = img.load()

#creating new image
newimg = Image.new("RGB", (304,92), "white") #since the current img width = 27968 ========> we know that 27968/304=92
newdat = newimg.load()

#getting each pixel and assigning value to it by rearranging the pixels in given file
linear_val=0
for w in range(304):
	for h in range(92):
		newdat[w,h] = imgdat[linear_val,0]
		linear_val+=1

#saving the new image
newimg.save("new.jpg")

#using tesseract to detect the text and print in command line
subprocess.call("tesseract new.jpg flag 2>/dev/null", shell=True)
subprocess.call("cat flag.txt|cut -c3-19", shell=True)

