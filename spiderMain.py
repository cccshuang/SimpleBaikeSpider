from spider.DataOutput import DataOutput
from spider.HtmlDownloader import HtmlDownloader
from spider.HtmlParser import HtmlParser
from spider.UrlManager import UrlManager


class SpiderMain(object):
    
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.ouput = DataOutput()
    
    def crawl(self,root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_urls_size() < 100):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls,data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.ouput.store_data(data)
                print('已经抓取%s个链接' %self.manager.old_urls_size())
            except Exception as e:
                print('crawl failed')
                print(e)
        self.ouput.output_html()

if __name__ == '__main__':
    spider_main = SpiderMain()
    spider_main.crawl("https://baike.baidu.com/item/Python/407313?fr=aladdin")
                