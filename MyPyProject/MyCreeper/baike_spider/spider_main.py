# -*- coding:utf-8 -*-
__author__ = 'luoxiao_y'
from baike_spider import url_mannager
from baike_spider import html_download
from baike_spider import html_outputer
from baike_spider import html_paser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_mannager.UrlMannager()
        self.downloader = html_download.HtmlDownloader()
        self.paser = html_paser.HtmlPaser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'caw %d: %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.paser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    print 'spider need to be closed'
                    break
                count += 1

            except:
                print 'caw failed'
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
