import urlparse
import re
compnents = urlparse.urlsplit('http://www.baidu.com/index/nnn/')
print compnents
print compnents.path
