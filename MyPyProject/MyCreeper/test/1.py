# -*- coding:utf-8 -*-
import urllib2 as ur
import re


def photo_cut(Internet_share):
    req = ur.urlopen(Internet_share)
    buf = req.read()
    list_url = re.findall(r'http:.+\.jpg', buf)
    i = 0
    for url in list_url:
        f= open(str(i)+'.jpg', 'wb')
        return_value = ur.urlopen(url)
        local_photo = return_value.read()
        f.write(local_photo)
        i += 1

if __name__ == '__main__':
    net = 'http://588ku.com/?h=bd'
    photo_cut(net)
