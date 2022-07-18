from entity.StockEntity import StockEntity
import psycopg2


class StockEntityRepository:
    def __init__(self):
        # self.conn = sqlite3.connect("C:/Users/PC/Desktop/stockTrading2/sqlite3.db")
        self.conn = psycopg2.connect(host="localhost", dbname="postgres", user="root", password="password")
        self.cur = self.conn.cursor()
        self.cur.execute("create table if not exists stocks("
                         "code varchar(255), "
                         "stocktype varchar(50), "
                         "date timestamp, "
                         "changerate float, "
                         "open bigint, "
                         "high bigint, "
                         "low bigint, "
                         "closing bigint, "
                         "volume bigint, "
                         "amount bigint)")
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

    def findByVolumeOrder(self, date, limit, ascending):
        if ascending:
            query = """
            select * from stocks
            where date = %s
            order by volume asc 
            limit %s
            """
            data = (str(date), limit)
            self.cur.execute(
                query,
                data
            )
            return self.cur.fetchall()
        else:
            query = """
                        select * from stocks
                        where date = %s
                        order by volume desc 
                        limit %s
                        """
            data = (str(date), limit)
            self.cur.execute(
                query,
                data
            )
            return self.cur.fetchall()




