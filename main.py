from modules.NewsCollecter import NewsCollecter
from modules.news.NewsProviderInfo import RSS_PROVIDER
from modules.database.NewsDBController import NewsDB

### init.
# database
ndb = NewsDB()
ndb.init()
# logging

nc = NewsCollecter()
nc.addNewsProvider(RSS_PROVIDER.MEAIL)

nc.start()
