# from datetime import datetime
# import os
import requests
import xml.etree.ElementTree as ET
from data.news import News

def getNewsFromMaeil(self, url):
    url = 'https://www.mk.co.kr/rss/30100041/'
    res = requests.get(url=url)
    result = []

    tree = ET.ElementTree(ET.fromstring(res.text))
    root = tree.getroot()
    for item in root.findall('./channel/item'):

        news = News(id      = item.find('no').text,
                    title   = item.find('title').text,
                    link    = item.find('link').text,
                    desc    = item.find('description').text)
        
        result.append(news)

    # rss_mk_file = f'rss_mk_{datetime.now().strftime("%Y%m%d%H%M%S")}.xml'     # 파일 검사해서 중복되는 데이터 제외 후 추가

    return result