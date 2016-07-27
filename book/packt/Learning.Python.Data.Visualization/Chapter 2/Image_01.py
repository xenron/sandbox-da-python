from pil import *
import Image
import ImageDraw
import os

def readcontent():
    '''Open the file to be read. Note the files permission is set to read-only.'''
    openFile = open('content.txt', 'r')
    '''Save the file's inner content to a Python Variable string.''' 
    readmeText = openFile.read() 
    '''Close the file to save memory.'''
    openFile.close() 
    '''Return the results to each as a reference variable.'''
    return openFile, readmeText 

def generateImage():
    '''Create our references.'''
    img = Image.new("RGBA", (100, 80), "white") 
    '''Draw the images size and background to the screen.'''
    draw = ImageDraw.Draw(img) 
    '''Position the text with an x/y of 10 x 10, assign it the text value and text color of red.'''
    output = draw.text((10, 10), readmeText,  fill=(255,0,0,255)) 
    '''Draw the text to the screen.'''
    draw = ImageDraw.Draw(img) 
    '''Save the image.'''
    img.save("output.png")
    '''Return the results to each as a reference variable.'''
    return draw, img, output 

'''trigger the read content function.'''
openFile, readmeText = readcontent() 

'''Generate our image.'''
draw, img, output = generateImage() 


