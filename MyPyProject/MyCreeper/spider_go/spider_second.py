# -*- coding:utf-8 -*-
import urllib2
import re
import itertools
import urlparse
import robotparser
import Throttle
from datetime import datetime
__author__ = 'luoxiao_y'


def download(url, user_agent='wswp', proxy=None, num_retries=2):
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
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
    for link in links:
        html = download(link)


def link_crawler(seed_url, link_regex, max_depth=1, scrape_callback=None):
    crawl_queue = [seed_url]
    seen = {seed_url: 0}
    rp = robotparser.RobotFileParser()
    while crawl_queue:
        url = crawl_queue.pop()
        rp.set_url(url+'/robots.txt')
        rp.read()
        user_agent = 'wswp'

        if rp.can_fetch(user_agent, url):
            throttle = Throttle.Throttle(5)
            throttle.wait(url)
            html = download(url)
            links = []
            if scrape_callback:
                links.extend(scrape_callback(url, html) or [])
            depth = seen[url]
            if depth != max_depth:
                for link in get_links(html):
                    if re.match(link_regex, link):
                        link = urlparse.urljoin(seed_url, link)
                        if link not in seen:
                            seen[link] = depth + 1
                            # seen.add(link)
                            crawl_queue.append(link)
        else:
            print 'Blocked by robots.txt:', url
                # print seen


def get_links(html):
    webpage_regex = re.compile(r'<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/(index|view)')