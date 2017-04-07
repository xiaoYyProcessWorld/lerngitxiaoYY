# -*- coding:utf-8 -*-
import urllib2 as ur
import cookielib as cook

url = "http://www.baidu.com"

print 'the first demo'
response1 = ur.urlopen(url)
print response1.getcode()
print len(response1.read())


print 'the second demo'
request = ur.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = ur.urlopen(request)
print response2.getcode()
print len(response2.read())

print 'the third demo'
cj = cook.CookieJar()
opener = ur.build_opener(ur.HTTPCookieProcessor(cj))
ur.install_opener(opener)
response3 = ur.urlopen(url)
print response3.getcode()
print cj
print response3.read()

