from entity.StockEntity import StockEntity
import psycopg2
import pandas as pd
import talib

from service.Utils import Utils


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
                         "close bigint, "
                         "volume bigint, "
                         "amount bigint)",
                         "primary key (code, date)"
                         )
        self.conn.commit()
        # DI
        self.utils = Utils()

    def deleteAll(self):
        query = """
        delete from stocks
        """
        self.cur.execute(query)
        self.conn.commit()


    def saveEntity(self, entity: StockEntity):
        query = """
                    insert into 
                    stocks (code, stocktype, date, changerate, open, high, low, close, volume, amount) 
                    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        data = (entity.code, entity.stockType, entity.date, entity.changeRate, entity.open, entity.high, entity.low,
                entity.close, entity.volume, entity.amount)
        if entity.high == 0 and entity.low == 0 and entity.close == 0 and entity.open == 0:
            pass
        else:
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

    def findByAmountOrder(self, date, limit, ascending):
        if ascending:
            query = """
            select * from stocks
            where date = %s
            order by amount asc
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
                        order by amount desc
                        limit %s
                        """
            data = (str(date), limit)
            self.cur.execute(
                query,
                data
            )
            return self.cur.fetchall()

    def findByChnageRateOrder(self, date, limit, ascending):
        if ascending:
            query = """
            select * from stocks
            where date = %s
            order by changerate asc
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
                        order by changerate desc
                        limit %s
                        """
            data = (str(date), limit)
            self.cur.execute(
                query,
                data
            )
            return self.cur.fetchall()

    def findByCci(self, date,  period, line):
        query = """
        select * from stocks
        where date <= (%s)::text::timestamptz
        order by date desc
        limit %s
        """
        data = (date, period)
        self.cur.execute(query, data)
        entities = self.cur.fetchall()

        dfList = [self.utils.tupleToStockEntity(i).toDict() for i in entities]
        df = pd.DataFrame.from_records(dfList)
        res = talib.CCI(
            df["high"],
            df["low"],
            df["close"],
            timeperiod=period
        )
        return res

    def findBySigma(self, date, period, line):
        query = """
                select * from stocks
                where date <= %s
                order by date desc
                limit %s
                """
        data = (date, period)
        self.cur.execute(query, data)
        entities = self.cur.fetchall()
        df = [i.toDict() for i in entities]

        res = df['close'].rolling(period).std()
        return res

    def findByParabolic(self, date, acceleration, maximum, upper):
        query = """
        select * from stocks
        where date <= %s
        order by date desc
        """
        data = date
        self.cur.execute(query, data)
        entities = self.cur.fetchall()
        df = [i.toDict() for i in entities]
        res = talib.SAR(
            df["high"],
            df["low"],
            acceleration=acceleration,
            maximum=maximum
        )
        return res

