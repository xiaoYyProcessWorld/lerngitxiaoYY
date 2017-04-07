# -*- coding:utf-8 -*-
__author__ = 'luoxiao_y'


class UrlMannager(object):
    def __init__(self):
        self.NewUrls = set()
        self.OldUrls = set()

    def add_new_url(self, root_url):
        if root_url is None:
            return
        if root_url not in self.NewUrls and root_url not in self.OldUrls:
            self.NewUrls.add(root_url)

    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for new_url in new_urls:
            self.add_new_url(new_url)

    def has_new_url(self):
        return len(self.NewUrls) != 0

    def get_new_url(self):
        new_url = self.NewUrls.pop()
        self.OldUrls.add(new_url)
        return new_url

