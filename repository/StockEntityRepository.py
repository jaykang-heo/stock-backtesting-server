from entity.StockEntity import StockEntity
import psycopg2
import sqlite3


class StockEntityRepository:
    def __init__(self):
        # self.conn = sqlite3.connect("C:/Users/PC/Desktop/stockTrading2/sqlite3.db")
        self.conn = psycopg2.connect(host="localhost", dbname="db", user="root", password="password")
        self.cur = self.conn.cursor()
        self.cur.execute("create table if not exists stocks("
                         "Code varchar(50), "
                         "StockType varchar(50), "
                         "Date varchar(50), "
                         "ChangeRate varchar(50), "
                         "Open varchar(50), "
                         "High varchar(50), "
                         "Low varchar(50), "
                         "Closing varchar(50), "
                         "Volume varchar(50), "
                         "Amount varchar(50))")
        self.conn.commit()

    def saveEntity(self, entity: StockEntity):
        self.cur.execute(
            "insert into stocks values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (entity.code, entity.stockType, entity.date, entity.changeRate, entity.open, entity.high, entity.low, entity.close, entity.volume, entity.amount)
        )
        self.conn.commit()

    def saveAllEntity(self, entities):
        pass

    def getEntityByCode(self, code):
        pass

    def existByCode(self, code):
        self.cur.execute(
            f"select * from stocks where code = {code}"
        )
        res = self.cur.fetchall()
        if len(res) != 0:
            return True
        else:
            return False

    def findAll(self):
        self.cur.execute("select * from stocks")
        return self.cur.fetchall()

    def findAllStocksByAmountDescending(self, limit):
        self.cur.execute(
            "select * from stocks order by Amount "

        )
        pass

    def findAllStocksByChangeRateDescending(self, limit):
        pass

    def findAllStocksByVolumeDescending(self, limit):
        pass


