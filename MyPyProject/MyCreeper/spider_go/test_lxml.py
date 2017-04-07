# -*- coding:utf-8 -*-
import urllib2
import re
import itertools
import urlparse
import robotparser
import Throttle
import spider_second
from bs4 import BeautifulSoup
import lxml.html
import cssselect
__author__ = 'luoxiao_y'
# broken_html = '<ul class=country><li>Area<li>Population</ul>'
# tree = html.fromstring(broken_html)
# fixed_html = html.tostring(tree, pretty_print=True)
# print fixed_html
url = 'http://example.webscraping.com/view/United-kingdom-239'
html = spider_second.download(url)
tree = lxml.html.fromstring(html)
td = tree.cssselect(r'tr#places_area__row > td.w2p_fw')[0]
area = td.text_content()
print area

