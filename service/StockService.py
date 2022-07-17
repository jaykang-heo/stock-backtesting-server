import datetime
import pandas as pd
import os

from entity.StockEntity import StockEntity
from repository.StockEntityRepository import StockEntityRepository
from service.infra.KiwoomService import KiwoomService
from service.infra.KrxService import KrxService


class StockService:
    def __init__(self):
        self.stockEntityRepository = StockEntityRepository()
        self.kiwoomService = KiwoomService(False)
        self.krxService = KrxService()

    @staticmethod
    def __getYearDates():
        date = datetime.date.today()
        year = str(date.year)
        month = str(date.month)
        day = str(date.day)
        sdate = datetime.date(2019, 3, 22)  # start date
        edate = datetime.date(date.year-1, date.month, date.day)
        return pd.date_range(sdate,edate-datetime.timedelta(days=1),freq='d').strftime('%Y%m%d').tolist()


    def synStocksFromKrxAndSave(self):
        dates = self.__getYearDates()
        for date in dates:
            print(date)
            stocks = self.krxService.findStocksByCode(date)
            print(len(stocks))
            for index, stock in stocks.iterrows():
                stockEntity = StockEntity(
                    code=stock.name,
                    stockType="",
                    changeRate=stock["등락률"],
                    date=date,
                    open=stock["시가"],
                    high=stock["고가"],
                    low=stock["저가"],
                    close=stock["종가"],
                    volume=stock["거래량"],
                    amount=stock["거래대금"]
                )
                self.stockEntityRepository.saveEntity(stockEntity)

    def syncStocksFromKiwoom(self):
        def __findStockFromKiwoomAndSave(self, code, type, date):
            codeStocks = self.kiwoomService.findStockByCode(code=code, date=date)
            for j in codeStocks:
                stockEntity = StockEntity(
                    code=j["종목코드"],
                    stockType=j[type],
                    changeRate=j[""],
                    date=j["일자"],
                    open=j["시가"],
                    high=j["고가"],
                    low=j["저가"],
                    close=j["현재가"],
                    volume=j["거래량"],
                    amount=j["거래대금"]
                )
                self.stockEntityRepository.saveEntity(stockEntity)
        # TODO: find latest date of code and sync
        kospiCodes = self.kiwoomService.getKospiCodes()
        kosdaqCodes = self.kiwoomService.getKosdaqCodes()
        date = datetime.date.today()
        year = str(date.year)
        month = str(date.month)
        day = str(date.day)
        if len(month) == 1:
            month = str("0"+str(month))
        if len(day) == 1:
            day = str("0"+str(day))
        targetDate = year+month+day
        for code in kospiCodes:
            # 423170
            __findStockFromKiwoomAndSave(code, "kospi", targetDate)
            # if not self.stockEntityRepository.existByCode(code):

        for code in kosdaqCodes:
            # if not self.stockEntityRepository.existByCode(code):
            __findStockFromKiwoomAndSave(code, "kosdaq", targetDate)


test = StockService()

test.synStocksFromKrxAndSave()



