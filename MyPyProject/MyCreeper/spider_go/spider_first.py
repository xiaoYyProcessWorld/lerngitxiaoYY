# -*- coding:utf-8 -*-
import urllib2
import re
import itertools
import time
__author__ = 'luoxiao_y'


def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <=600:
                download(url, user_agent, num_retries-1)
    return html


def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall(r'<loc>(.*?)</loc>', sitemap)
    print links
    for link in links:
        html = download(link)
        # time.sleep(10)
        # return html


if __name__ == '__main__':
    # print len(download('http://www.baidu.com'))
    # print download('http://httpstat.us/500')
    print crawl_sitemap('http://example.webscraping.com/sitemap.xml')



    # max_errors = 5
    # num_errors = 0
    # for page in itertools.count(1):
    #     url = 'http://example.webscraping.com/view/-%d' % page
    #     html = download(url)
    #     if html is None:
    #         num_errors += 1
    #         if num_errors == max_errors:
    #             break
    #     else:
    #         num_errors = 0
    # print download('http://www.12306.cn')
