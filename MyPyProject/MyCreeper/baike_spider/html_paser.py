# -*- coding:utf-8 -*-
import re
import urlparse

__author__ = 'luoxiao_y'
from bs4 import BeautifulSoup


class HtmlPaser(object):
    def _get_new_urls(self, soup):
        new_urls = set()
        url = 'http://baike.baidu.com/item'
        links = soup.find_all(name='a', href=re.compile(r'(/Python1#[\d]+)|(/[\w]*Py[\w]+)'))
        for link in links:
            new_new_url = link['href']
            new_full_url = urlparse.urljoin(url, new_new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_conts(self, new_url, soup):
        res_data = {}

        res_data['url'] = new_url
#        <dd class="lemmaWgt-lemmaTitle-title">
#       <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()
#       <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        print res_data
        return res_data

    def parse(self, new_url, html_cont):
        if new_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(soup)
        new_conts = self._get_new_conts(new_url, soup)
        return new_urls, new_conts


    
    