# -*- coding:utf-8 -*-
import urllib2
import re
import itertools
import urlparse
import robotparser
import datetime
import time

__author__ = 'luoxiao_y'


class Throttle(object):
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now()-last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain]=datetime.datetime.now()