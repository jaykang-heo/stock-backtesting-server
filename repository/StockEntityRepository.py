from entity.StockEntity import StockEntity
import psycopg2


class StockEntityRepository:
    def __init__(self):
        # self.conn = sqlite3.connect("C:/Users/PC/Desktop/stockTrading2/sqlite3.db")
        self.conn = psycopg2.connect(host="localhost", dbname="postgres", user="root", password="password")
        self.cur = self.conn.cursor()
        self.cur.execute("create table if not exists stocks("
                         "code varchar(50), "
                         "stocktype varchar(50), "
                         "date varchar(50), "
                         "changerate varchar(50), "
                         "open varchar(50), "
                         "high varchar(50), "
                         "low varchar(50), "
                         "closing varchar(50), "
                         "volume varchar(50), "
                         "amount varchar(50))")
        self.conn.commit()

    def saveEntity(self, entity: StockEntity):
        query = """
            insert into 
            stocks (code, stocktype, date, changerate, open, high, low, closing, volume, amount) 
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
        data = (entity.code, entity.stockType, entity.date, entity.changeRate, entity.open, entity.high, entity.low, entity.close, entity.volume, entity.amount)
        self.cur.execute(
            query,
            data
        )
        self.conn.commit()

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


