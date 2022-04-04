from typing import overload
import mariadb
import sys
import conf.cfgParser as cp

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)

        return super().__call__(*args, **kwds)


class MariaDBManager(metaclass=MetaSingleton):
    _connection = None
    _cur = None

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

            return self._cur
            
        except mariadb.Error as e:
            print(f"Error connecting to the database: {e}")
            sys.exit(1)


    def createNaesTable(self, table_name):
        self._cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (index INT NOT NULL AUTO_INCREMENT, name VARCHAR(30) NOT NULL)")
            # index INT NOT NULL AUTO_INCREMENT, \
            # id VARCHAR(15) NOT NULL, \
            # title VARCHAR(30) NOT NULL, \
            # contents VARCHAR(100), \
            # link VARCHAR(50), \
            # PRIMARY KEY (id))")

# CREATE TABLE animals (
#      id MEDIUMINT NOT NULL AUTO_INCREMENT,
#      name CHAR(30) NOT NULL,
#      PRIMARY KEY (id)
# );


    def addNewsData(self, id, title, contents, link):
        try:
            self._cur.execute("INSERT INTO mytable SET id={}, title={}, contents={}, link={}".format(id, title, contents, link))
        except:
            print("[WARN] fail to insert news data")

