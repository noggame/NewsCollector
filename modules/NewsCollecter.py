import modules.news.NewsProviderInfo as NP
from modules.news.rss.RSS import RSS


class NewsCollecter:
    def __init__(self) -> None:
        self._newsProviderList = set()

    def addNewsProvider(self, rss:NP):
        self._newsProviderList.add(rss)

    def start(self):
        
        # @@@@@ get data / tich = 1min

        for provider in self._newsProviderList:

            if type(provider) == NP.RSS_PROVIDER:
                rss_name = NP.RSS_PROVIDER(provider).name

                # rss info.
                rss:RSS = NP.RSS_PROVIDER[rss_name].value
                rss_url = NP.URL[rss_name].value

                # collecting data
                rss.getRssData(rss_url)
            
            else:   # case for formats isn't implemented RSS
                print("need to implement...")

            # colleting data


