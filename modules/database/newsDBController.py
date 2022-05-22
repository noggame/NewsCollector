import json
import mariadb
import sys
import conf.cfgParser as cfg
from data.NewsInfo import NewsData
from modules.DesignPattern import MetaSingleton

class NewsDB(metaclass=MetaSingleton):
    _connection = None
    _cur = None

    def init(self):
        self.connect()
        self.createNewsTable(cfg.get('mysql', 'table_news'))

    def connect(self):
        try:
            if not self._connection:
                self._connection = mariadb.connect(
                    user = cfg.get('mysql', 'user'),
                    password = cfg.get('mysql', 'password'),
                    host = cfg.get('mysql', 'host'),
                    port = int(cfg.get('mysql', 'port')),
                    database = cfg.get('mysql', 'database')
                )
                self._cur = self._connection.cursor()
            
        except mariadb.Error as e:
            print(f"Error connecting to the database: {e}")
            sys.exit(1)


    def createNewsTable(self, table_name):
        self._cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (\
            id VARCHAR(15) NOT NULL, \
            title TEXT NOT NULL, \
            contents TEXT, \
            link TEXT, \
            registered DATETIME, \
            PRIMARY KEY (id))")


    # 중복된 데이터 제외하고 추가
    def addNewsData(self, newsData:NewsData):
        try:
            self._cur.execute("INSERT IGNORE INTO {} SET id='{}', title='{}', contents='{}', link='{}', registered=NOW()".format(cfg.get('mysql', 'table_news'), newsData.id, str(newsData.title).replace("'", "''"), str(newsData.desc).replace("'", "''"), newsData.link))
            self._connection.commit()
        except mariadb.Error as e:
            print(f"[WARN] fail to insert news data - {e}")


    def getNewsDataFromID(self, id:str):
        try:
            data:NewsData = None
            self._cur.execute("SELECT * FROM {} WHERE id='{}'".format(cfg.get('mysql', 'table_news'), id))
            for findData in self._cur:
                data = NewsData(id=findData[0], title=findData[1], desc = findData[2], link=findData[3])
                return data

        except mariadb.Error as e:
            print(f"[WARN] fail to get news data")

        print("[Info] Not found {} from {}".format(id, cfg.get('mysql', 'table_news')))
        return None


    # TODO: getNewsData(self, number:int) -> n개의 뉴스데이터 반환 (시간순)


    # TODO: limitData(self, tableName:string, number:int) -> tableName 테이블의 데이터 개수를 number개로 제한
    def limitData(self, tableName:str, limit:int):
        count = 0

        self._cur.execute("SELECT COUNT(*) FROM {}".format(cfg.get('mysql', 'table_news')))
        for data in self._cur:
            count = data[0]

        if count > limit:
            count -= limit
            self._cur.execute("DELETE FROM {} ORDER BY registered LIMIT {}".format(cfg.get('mysql', 'table_news'), count))
            self._connection.commit()