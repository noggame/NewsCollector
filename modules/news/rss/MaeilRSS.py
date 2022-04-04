from datetime import datetime
import os
import re
import requests
import xml.etree.ElementTree as ET
# from modules.news.NewsProviderInfo import News
from data.NewsInfo import NewsInfo
from modules.news.rss.RSS import RSS

class MaeilNews(RSS):

    def getRssData(url:str):

        response = requests.get(url=url)
        result = []

        if response.status_code == 200:
            tree = ET.ElementTree(ET.fromstring(response.text))
            root = tree.getroot()

            for item in root.findall('./channel/item'):   # get items under channel

                news = NewsInfo(id      = re.sub('[/]', '', item.find('no').text),      # YYYYMM#####
                                title   = item.find('title').text,
                                link    = item.find('link').text,
                                desc    = item.find('description').text)
                
                result.append(news)

        else:
            print("bad response : {}".format(response.status_code))


        ### 파일 검사해서 중복되는 데이터 제외 후 추가
        # rss_mk_file = f'rss_mk_{datetime.now().strftime("%Y%m%d%H%M%S")}.xml'     

        return result

    def getNewsInfo(news:NewsInfo):
        if not NewsInfo:
            return None
        
        ### DB (news_list) #########################
        # id, publisher, title, link, summary, reg
        ############################################
        
        # db 검색 (with news.id)
        
        
        # DB에 없으면 해당 링크에서 정보 파싱 및 업데이트
        return None