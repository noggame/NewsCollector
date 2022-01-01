from datetime import datetime
import os
import re
import requests
import xml.etree.ElementTree as ET
from data.news import News

def getRSSdata(url:str='https://www.mk.co.kr/rss/30100041/'):
    url = url
    res = requests.get(url=url)
    result = []

    tree = ET.ElementTree(ET.fromstring(res.text))
    root = tree.getroot()
    for item in root.findall('./channel/item'):

        news = News(id      = re.sub('[/]', '', item.find('no').text),      # YYYYMM#####
                    title   = item.find('title').text,
                    link    = item.find('link').text,
                    desc    = item.find('description').text)
        
        result.append(news)


    # rss_mk_file = f'rss_mk_{datetime.now().strftime("%Y%m%d%H%M%S")}.xml'     # 파일 검사해서 중복되는 데이터 제외 후 추가

    return result

def getNewsInfo(news:News):
    if not News:
        return None
    
    ### DB (news_list) #########################
    # id, publisher, title, link, summary, reg
    ############################################
    
    # db 검색 (with news.id)
    
    
    # DB에 없으면 해당 링크에서 정보 파싱 및 업데이트
    return None