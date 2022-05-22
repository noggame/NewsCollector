from time import sleep
import time
import modules.news.NewsProviderInfo as NP
from modules.news.rss.RSS import RSS
from modules.database.NewsDBController import NewsDB as ndb
import conf.cfgParser as cfg

class NewsCollecter:
    def __init__(self) -> None:
        self._newsProviderList = set()

    def addNewsProvider(self, rss:NP):
        self._newsProviderList.add(rss)

    def start(self):
        while True:

            for provider in self._newsProviderList:

                if type(provider) == NP.RSS_PROVIDER:
                    rss_name = NP.RSS_PROVIDER(provider).name

                    # rss info.
                    rss:RSS = NP.RSS_PROVIDER[rss_name].value
                    rss_url = NP.URL[rss_name].value

                    # collecting data
                    newsList = rss.getRssData(rss_url)
                    if not newsList:
                        continue
                    
                    for newsData in newsList:
                        ndb().addNewsData(newsData)
                    print("[SUCCESS] {} data is stored on NewsDB".format(rss_name))
                
                else:   # case for formats isn't implemented RSS
                    print("need to implement...")


                time.sleep(int(cfg.get('crawl', 'tick')))  # time tick

            ndb().limitData(cfg.get('mysql', 'table_news'), 10000)