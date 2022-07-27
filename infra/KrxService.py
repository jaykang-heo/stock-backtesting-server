from logging import exception

from pykrx import stock as krxAPI
import pandas as pd
import time


class KrxService:
    def __init__(self):
        pass

    def findStocksByCode(self, date):
        kospi = pd.DataFrame()
        kosdaq = pd.DataFrame()
        time.sleep(1)
        try:
            kospi = krxAPI.get_market_ohlcv(date, market="KOSPI")
        except Exception as e:
            print("Get KOSPI market data failed", date, e)
        try:
            kosdaq = krxAPI.get_market_ohlcv(date, market="KOSDAQ")
        except Exception as e:
            print("Get KOSDAQ market data failed", date, e)
        return pd.concat([kospi, kosdaq])

    def getValidBusinessDays(self, fromDate, toDate):
        dates = krxAPI.get_previous_business_days(fromdate=fromDate, todate=toDate)
        res = [i.strftime('%Y%m%d') for i in dates]
        return res
