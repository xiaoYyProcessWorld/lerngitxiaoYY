# -*- coding:utf-8 -*-
import urllib2
import re
import itertools
import urlparse
import robotparser
import Throttle
import spider_second
from bs4 import BeautifulSoup
import time
__author__ = 'luoxiao_y'

# broken_html = '<ul class=country><li>Area<li>Population</ul>'
# soup = BeautifulSoup(broken_html, 'html.parser')
# fixed_html = soup.prettify()
# print fixed_html
#
# url = 'http://example.webscraping.com/vie9w/United-kingdom-239'
# html = spider_second.download(url)
# soup = BeautifulSoup(html, 'html.parser')
# tr = soup.find(attrs={'id': 'places_area__row'})
# td = tr.find(attrs={'class': 'w2p_fw'})
# print td
# area = td.text
# print area

i = time.time()
print i

