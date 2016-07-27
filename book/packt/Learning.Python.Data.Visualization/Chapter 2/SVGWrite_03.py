import svgwrite
def readcontent():
	'''Open the file to be read. Note the file's permission is set to read-only.'''
	openFile = open('content.txt', 'r') 
	
	readmeText = openFile.read() 
	'''Save the file's inner content to a Python Variable string.'''
	
	openFile.close() 
	'''Close the file to save memory.'''
	
	return openFile, readmeText 
	'''Return the results to each as a reference variable.'''


def createSVGText(usrname):
    drawObj = svgwrite.Drawing('username.svg', profile='tiny', width=444, height=300)
    drawObj.add(drawObj.text(usrname, insert=(15, 64), fill='red', font_size=70, font_family='sans-serif', font_weight='bold'))
    drawObj.add(drawObj.line((10, 10), (10, 70), stroke=svgwrite.rgb(0, 0, 0, '%')))
    drawObj.add(drawObj.line((10, 70), (400, 70), stroke=svgwrite.rgb(0, 0, 0, '%')))
    drawObj.save()
    return drawObj

'''trigger the read content function.'''
openFile, readmeText = readcontent() 

'''Grab the 'readmeText' file content and pass that into our createSVGText function.'''
drawObj = createSVGText(readmeText) 