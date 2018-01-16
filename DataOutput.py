import codecs

class DataOutput(object):
    
    def __init__(self):
        self.datas = []
    
    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        
    def output_html(self):
        fout = codecs.open('baike.html', 'w', encoding='utf-8') #python中默认的编码是ascii，如果直接使用open方法得到文件对象然后进行文件的读写，都将无法使用包含中文字符（以及其他非ascii码字符），因此建议使用utf-8编码
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' %data['url'])
            fout.write('<td>%s</td>' %data['title'])
            fout.write('<td>%s</td>' %data['summary'])
            fout.write('</tr>')
            self.datas.remove(data)
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
        