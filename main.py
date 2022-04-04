from modules.NewsCollecter import NewsCollecter
from modules.news.NewsProviderInfo import RSS_PROVIDER


nc = NewsCollecter()
nc.addNewsProvider(RSS_PROVIDER.MEAIL)

nc.start()
# print(NewsProvider._member_map_['MEAIL']._value_)


# mk.getRSSdata("https://www.mk.co.kr/rss/30100041/")

# for item in mk.getRSSdata("https://www.mk.co.kr/rss/30100041/"):
#     print(item)
