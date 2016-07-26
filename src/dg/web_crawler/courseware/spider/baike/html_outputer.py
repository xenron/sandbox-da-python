# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:09:01 2016

@author: Administrator
"""

class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        
        
    def output_html(self):      
        for data in self.datas:
            name =  data['title']+'.html'
            fout = open (name,'w')
            fout.write("<html>")
            fout.write("<body>")
            fout.write("<div _class='url'>%s</div>" % data['url'])
            fout.write("<div _class=title>%s</div>" % data['title'].encode('utf-8'))
            fout.write('<div _class="content">')
            for i in range(len(data['content'])):
                fout.write("<div>%s</div>" % data['content'][i].encode('utf-8'))
            fout.write("</div>")
            fout.write("</body>")
            fout.write("</html>")
            
            fout.close()
        
        
        