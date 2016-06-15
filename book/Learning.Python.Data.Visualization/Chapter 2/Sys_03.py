import os

openFile = os.open('PyREADME.txt', os.O_RDONLY ) #Open the file to be read.

#Save the file's inner content to a Python Variable string.  This take two parameters, the file to be opened and how many characters to read.

readmeText = os.read(openFile, 100) 

print(readmeText)

