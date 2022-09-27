from entity.stock_entity import StockEntity
import psycopg2
import pandas as pd
import talib

from service.utils import Utils


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
        self.cur.execute("create table if not exists fdr_stocks("
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
                         "primary key(code, date)"
                         )
        self.conn.commit()
        # DI
        self.utils = Utils()

    def delete_all(self):
        query = """
        delete from stocks
        """
        self.cur.execute(query)
        self.conn.commit()

    def save_entity(self, type, entity: StockEntity):
        if type == 'PYKRX':
            query = """
                        insert into 
                        stocks (code, stocktype, date, changerate, open, high, low, close, volume, amount) 
                        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        on conflict (%s, %s)
                        do nothing
                        """
            data = (entity.code, entity.stockType, entity.date, entity.changerate, entity.open, entity.high, entity.low,
                    entity.close, entity.volume, entity.amount, entity.code, entity.date)
            if entity.high == 0 and entity.low == 0 and entity.close == 0 and entity.open == 0:
                pass
            else:
                self.cur.execute(
                    query,
                    data
                )
                self.conn.commit()
        elif type == "FDR":
            query = """
                insert into 
                fdr_stocks (code, stocktype, date, changerate, open, high, low, close, volume, amount) 
                values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            data = (entity.code, entity.stockType, entity.date, entity.changerate, entity.open, entity.high, entity.low,
                    entity.close, entity.volume, entity.amount)
            if entity.high == 0 and entity.low == 0 and entity.close == 0 and entity.open == 0:
                pass
            else:
                self.cur.execute(
                    query,
                    data
                )
                self.conn.commit()


    def find_by_volume_order(self, date, limit, ascending):
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

    def find_by_amount_order(self, date, limit, ascending):
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

    def find_by_changerate_order(self, date, limit, ascending):
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

    def find_by_cci(self, date, code, period, line, comp):
        query = """
        select * from stocks
        where date <= (%s)::text::timestamptz
        and code = (%s)
        order by date desc
        limit %s
        """
        data = (date, code, period)
        self.cur.execute(query, data)
        entities = self.cur.fetchall()
        dfList = [self.utils.tupleToStockEntity(i).toDict() for i in entities[::-1]]
        df = pd.DataFrame.from_records(dfList)
        res = talib.CCI(
            high=df["high"],
            low=df["low"],
            close=df["close"],
            timeperiod=period
        )
        value = res.iloc[-1]
        if comp:
            if value >= line:
                return entities[0]
        else:
            if value < line:
                return entities[0]

    def find_by_sigma(self, date, code, period, line):
        query = """
                select * from stocks
                where date <= (%s)::text::timestamptz
                and code = %s
                order by date desc
                limit %s
                """
        data = (date, code, period)
        self.cur.execute(query, data)
        entities = self.cur.fetchall()
        dfList = [self.utils.tupleToStockEntity(i).toDict() for i in entities]
        df = pd.DataFrame.from_records(dfList)
        res = df['close'].rolling(period).std()
        return res

    def find_by_psar_upper(self, date, code, acceleration, maximum, upper):
        query = """
        select * from stocks
        where date <= (%s)::text::timestamptz
        and code = %s
        order by date desc
        """
        data = (date, code)
        self.cur.execute(query, data)
        entities = self.cur.fetchall()
        dfList = [self.utils.tupleToStockEntity(i).toDict() for i in entities[::-1]]
        df = pd.DataFrame.from_records(dfList)
        res = talib.SAR(
            high=df["high"],
            low=df["low"],
            acceleration=acceleration,
            maximum=maximum
        )
        entity = self.utils.tupleToStockEntity(entities[0])
        if entity.high >= res.iloc[-1]:
            return entities[0]

    def find_stocks_by_codes_and_order_by_volume_descending(self, date, codes):
        query = """
                select * from stocks
                where date = (%s)::text::timestamptz
                and code = any(%s)
                order by volume desc
                """
        data = (date, codes)
        self.cur.execute(query, data)
        entities = self.cur.fetchall()
        return entities

