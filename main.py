from modules.NewsCollecter import NewsCollecter
from modules.news.NewsProviderInfo import RSS_PROVIDER
from modules.database.NewsDBController import NewsDB
import logging
import os
from datetime import datetime

# logging.basicConfig(filename=f'{os.getcwd()}/logs/log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

### database
ndb = NewsDB()
ndb.init()

### collecting news
nc = NewsCollecter()
nc.addNewsProvider(RSS_PROVIDER.MEAIL)
nc.start()


### limit test
# ndb.limitData('newsinfo', 5)