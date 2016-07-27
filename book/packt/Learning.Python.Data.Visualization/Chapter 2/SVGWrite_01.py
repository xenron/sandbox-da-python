import svgwrite

drawObj = svgwrite.Drawing('username.svg', profile='tiny', width=444, height=300)
drawObj.add(drawObj.text('Test', insert=(15, 64), fill='red', font_size=70, font_family='sans-serif', font_weight='bold'))
drawObj.add(drawObj.line((10, 10), (10, 70), stroke=svgwrite.rgb(0, 0, 0, '%')))
drawObj.add(drawObj.line((10, 70), (370, 70), stroke=svgwrite.rgb(0, 0, 0, '%')))
drawObj.save()
