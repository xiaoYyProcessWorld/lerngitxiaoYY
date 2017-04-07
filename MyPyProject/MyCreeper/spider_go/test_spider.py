# -*- coding:utf-8 -*-
import urllib2
import re
import itertools
import urlparse
import robotparser
__author__ = 'luoxiao_y'
import spider_second
#
# rp = robotparser.RobotFileParser()
# rp.set_url('http://example.webscraping.com/robots.txt')
# print rp.read()
# user_agent = 'wssp'
# print rp.can_fetch(user_agent, 'http://example.webscraping.com')

url = 'http://example.webscraping.com/view/United-kingdom-239'
html = spider_second.download(url)
# print html
print re.findall(r'<tr id="places_area__row">'
                 r'<td class="w2p_fl"><label for="places_area" '
                 r'id="places_area__label">Area: </label></td><td class="w2p_fw">(.*?)</td>', html)

print re.findall(r'<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)
# print re.findall(r'<td class="w2p_fw">(.*?)</td>', html)[1]

