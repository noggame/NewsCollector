from datetime import datetime
import os
import re
import requests
import xml.etree.ElementTree as ET
# from modules.news.NewsProviderInfo import News
from data.NewsInfo import NewsData
from modules.news.rss.RSS import RSS

class MaeilNews(RSS):

    def getRssData(url:str):

        response = requests.get(url=url)
        result = []

        if response.status_code == 200:
            tree = ET.ElementTree(ET.fromstring(response.text))
            root = tree.getroot()

            for item in root.findall('./channel/item'):   # get items under channel

                news = NewsData(id      = re.sub('[/]', '', item.find('no').text),      # YYYYMM#####
                                title   = item.find('title').text,
                                link    = item.find('link').text,
                                desc    = item.find('description').text)
                
                result.append(news)

        else:
            print("bad response : {}".format(response.status_code))

        return result
