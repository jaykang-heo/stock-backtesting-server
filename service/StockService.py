from entity.StockEntity import StockEntity
from repository.StockEntityRepository import StockEntityRepository
from infra.KrxService import KrxService
from service.Utils import Utils
import datetime


class StockService:
    def __init__(self):
        self.stockEntityRepository = StockEntityRepository()
        self.stockEntityRepository.deleteAll()
        self.krxService = KrxService()
        self.utils = Utils()

    def syncStocksFromKrxAndSave(self):
        # dates = self.utils.getYearDates()
        today = datetime.date.today().strftime('%Y%m%d')
        validDates = self.krxService.getValidBusinessDays(fromDate=19850101, toDate=today)
        for date in validDates:
            stocks = self.krxService.findStocksByCode(date)
            print(date, len(stocks))
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



