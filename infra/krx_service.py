from logging import exception

from pykrx import stock as krxAPI
import pandas as pd
import time


class KrxService:
    def __init__(self):
        pass

    def get_stock_codes(self):
        date = krxAPI.get_nearest_business_day_in_a_week()
        kospi = krxAPI.get_market_ticker_list(date, "KOSPI")
        kosdaq = krxAPI.get_market_ticker_list(date, "KOSDAQ")
        return kospi + kosdaq

    @staticmethod
    def find_stocks_by_code(date):
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

    @staticmethod
    def get_valid_business_days(from_date, to_date):
        dates = krxAPI.get_previous_business_days(fromdate=from_date, todate=to_date)
        res = [i.strftime('%Y%m%d') for i in dates]
        return res
