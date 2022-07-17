from pykrx import stock
import time

class KrxService:
    def __init__(self):
        pass

    def findStocksByCode(self, date):
        time.sleep(1)
        kospi = stock.get_market_ohlcv(date, market="KOSPI")
        kosdaq = stock.get_market_ohlcv(date, market="KOSDAQ")
        return kospi.append(kosdaq)
