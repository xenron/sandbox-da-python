import svgwrite

def readcontent():
    '''Open the file to be read. Note the file's permission is set to read-only.'''
    openFile = open('content.txt', 'r') 
    '''Save the file's inner content to a Python Variable string.'''
    readmeText = openFile.read() 
    '''Close the file to save memory.'''
    openFile.close() 
    '''Return the results to each as a reference variable.'''
    return openFile, readmeText 

'''trigger the read content function.'''
openFile, readmeText = readcontent() 