import datetime
import pandas as pd

from entity.StockEntity import StockEntity
from repository.StockEntityRepository import StockEntityRepository
from infra.KrxService import KrxService


class StockService:
    def __init__(self):
        self.stockEntityRepository = StockEntityRepository()
        self.krxService = KrxService()

    @staticmethod
    def __getYearDates():
        date = datetime.date.today()
        # sdate = datetime.date(2019, 3, 22)  # start date
        sdate = datetime.date(date.year, date.month, date.day)  # start date
        # edate = datetime.date(date.year-1, date.month, date.day)
        # edate = datetime.date(2019, 3, 23)
        # return pd.date_range(sdate, edate-datetime.timedelta(days=1), freq='d').strftime('%Y%m%d').tolist()
        return pd.date_range(sdate, sdate, freq='d').strftime('%Y%m%d').tolist()

    def syncStocksFromKrxAndSave(self):
        dates = self.__getYearDates()
        for date in dates:
            print(date)
            stocks = self.krxService.findStocksByCode(date)
            print(len(stocks))
            for index, stock in stocks.iterrows():
                stockEntity = StockEntity(
                    code=stock.name,
                    stockType="",
                    changeRate=float(stock["등락률"]),
                    date=date,
                    open=int(stock["시가"]),
                    high=int(stock["고가"]),
                    low=int(stock["저가"]),
                    close=int(stock["종가"]),
                    volume=int(stock["거래량"]),
                    amount=int(stock["거래대금"])
                )
                self.stockEntityRepository.saveEntity(stockEntity)

test = StockService()
test.syncStocksFromKrxAndSave()



