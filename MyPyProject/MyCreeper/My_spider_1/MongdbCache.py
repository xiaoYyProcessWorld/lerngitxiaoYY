import re
import urlparse
import shutil
import zlib
import csv
import lxml.html
try:
    import cPickle as pickle
except ImportError:
    import pickle
import zlib
from bson.binary import Binary
from datetime import datetime, timedelta
from pymongo import MongoClient
from link_crawler import link_crawler

#
class MongdbCache(object):
    def __init__(self, client=None, expires=timedelta(days=30)):
        self.client = MongoClient('localhost', 27017)if client is None else client
        self.db = self.client.cache
        self.db.webpage.create_index('timestamp', expireAfterSeconds=expires.total_seconds())

    def __contains__(self, url):
        try:
            self[url]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, url):
        record = self.db.webpage.find_one({'_id': url})
        if record:
            return pickle.loads(zlib.decompress(record['result']))
        else:
            raise KeyError(url + 'does not exist')

    def __setitem__(self, url, result):
        record = {'result': Binary(zlib.compress(pickle.dumps(result))), 'timestamp': datetime.utcnow()}
        self.db.webpage.update({'_id', url}, {'$set': record}, upsert=True)

    def clear(self):
        self.db.webpage.drop()

#
# class MongoCache:
#     """
#     Wrapper around MongoDB to cache downloads
#
#     >>> cache = MongoCache()
#     >>> cache.clear()
#     >>> url = 'http://example.webscraping.com'
#     >>> result = {'html': '...'}
#     >>> cache[url] = result
#     >>> cache[url]['html'] == result['html']
#     True
#     >>> cache = MongoCache(expires=timedelta())
#     >>> cache[url] = result
#     >>> # every 60 seconds is purged http://docs.mongodb.org/manual/core/index-ttl/
#     >>> import time; time.sleep(60)
#     >>> cache[url]
#     Traceback (most recent call last):
#      ...
#     KeyError: 'http://example.webscraping.com does not exist'
#     """
#     def __init__(self, client=None, expires=timedelta(days=30)):
#         """
#         client: mongo database client
#         expires: timedelta of amount of time before a cache entry is considered expired
#         """
#         # if a client object is not passed
#         # then try connecting to mongodb at the default localhost port
#         self.client = MongoClient('localhost', 27017) if client is None else client
#         #create collection to store cached webpages,
#         # which is the equivalent of a table in a relational database
#         self.db = self.client.cache
#         self.db.webpage.create_index('timestamp', expireAfterSeconds=expires.total_seconds())
#
#     def __contains__(self, url):
#         try:
#             self[url]
#         except KeyError:
#             return False
#         else:
#             return True
#
#     def __getitem__(self, url):
#         """Load value at this URL
#         """
#         record = self.db.webpage.find_one({'_id': url})
#         if record:
#             #return record['result']
#             return pickle.loads(zlib.decompress(record['result']))
#         else:
#             raise KeyError(url + ' does not exist')
#
#
#     def __setitem__(self, url, result):
#         """Save value for this URL
#         """
#         #record = {'result': result, 'timestamp': datetime.utcnow()}
#         record = {'result': Binary(zlib.compress(pickle.dumps(result))), 'timestamp': datetime.utcnow()}
#         self.db.webpage.update({'_id': url}, {'$set': record}, upsert=True)
#
#
#     def clear(self):
#         self.db.webpage.drop()
# #

class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open('countries.csv', 'wb'))
        self.fields = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code',
                       'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
        self.writer.writerow(self.fields)

    def __call__(self, url, html):
        if re.search('/view/', url):
            tree = lxml.html.fromstring(html)
            row = []
            for field in self.fields:
                row.append(tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content())
                # print row
            self.writer.writerow(row)


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com/', '/(index|view)', scrape_callback=ScrapeCallback(),
                 cache=MongoClient())
