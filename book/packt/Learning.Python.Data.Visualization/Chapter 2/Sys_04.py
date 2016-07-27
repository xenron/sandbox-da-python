import os

txtContent = 'Hello World'
openFile = open('content.txt', 'w') #Open the file to be written.
readmeText = openFile.write(txtContent) #Write the file's inner content to the text file.

openFile.close() #Close the file.
