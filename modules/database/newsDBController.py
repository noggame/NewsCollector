import json
import mariadb
import sys
import conf.cfgParser as cp
from data.NewsInfo import NewsInfo
from modules.DesignPattern import MetaSingleton

class NewsDB(metaclass=MetaSingleton):
    _connection = None
    _cur = None

    def init(self):
        self.connect()
        self.createNewsTable(cp.get('mysql', 'table'))

    def connect(self):
        try:
            if not self._connection:
                self._connection = mariadb.connect(
                    user = cp.get('mysql', 'user'),
                    password = cp.get('mysql', 'password'),
                    host = cp.get('mysql', 'host'),
                    port = int(cp.get('mysql', 'port')),
                    database = cp.get('mysql', 'database')
                )
                self._cur = self._connection.cursor()
            
        except mariadb.Error as e:
            print(f"Error connecting to the database: {e}")
            sys.exit(1)


    def createNewsTable(self, table_name):
        self._cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (\
            idx INT NOT NULL AUTO_INCREMENT, \
            id VARCHAR(15) NOT NULL, \
            title TEXT NOT NULL, \
            contents TEXT, \
            link TEXT, \
            PRIMARY KEY (idx, id))")


    def addNewsData(self, newsData:NewsInfo):
        try:
            self._cur.execute("INSERT INTO {} SET id='{}', title='{}', contents='{}', link='c'".format(cp.get('mysql', 'table'), newsData.id, str(newsData.title).replace("'", "''"), str(newsData.desc).replace("'", "''"), newsData.link))
            self._connection.commit()
        except mariadb.Error as e:
            print(f"[WARN] fail to insert news data - {e}")


