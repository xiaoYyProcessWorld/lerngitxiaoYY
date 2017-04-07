
from pymongo import MongoClient
from My_spider_1.MongdbCache import MongdbCache
from datetime import datetime, timedelta
#
# client = MongoClient('localhost', 27017)
# url = 'http://example.webscraping.com/view/United-Kingdom-239'
# html = '...'
# db = client.cache
# db.webpage.update({'_id': url}, {'$set': {'html':html}}, upsert=True)
# print db.webpage.find_one({'_id': url})
# new_html = 'http://www.baidu.com'
# db.webpage.update({'_id': url}, {'$set': {'html': new_html}}, upsert=True)
# print db.webpage.find_one({'_id': url})
# print db.webpage.find({'_id': url}).count()
#
#
#
# cache = MongdbCache(expires=timedelta())
# result = {'html': '...'}
# cache[url] = result
# print cache[url]
# # client = pymongo.MongoClient('localhost', 27017)
# # db = client.cache



