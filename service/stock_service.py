from entity.stock_entity import StockEntity
from repository.stock_entity_repository import StockEntityRepository
from infra.krx_service import KrxService
from service.utils import Utils
import datetime


class StockService:
    def __init__(self):
        self.stockEntityRepository = StockEntityRepository()
        self.stockEntityRepository.delete_all()
        self.krxService = KrxService()
        self.utils = Utils()

    def syncStocksFromKrxAndSave(self):
        # dates = self.utils.getYearDates()
        today = datetime.date.today().strftime('%Y%m%d')
        validDates = self.krxService.get_valid_business_days(from_date=20220401, to_date=today)
        for date in validDates:
            stocks = self.krxService.find_stocks_by_code(date)
            print(date, len(stocks))
            for index, stock in stocks.iterrows():
                stockEntity = StockEntity(
                    code=stock.name,
                    stock_type="",
                    changerate=float(stock["등락률"]),
                    date=date,
                    open=int(stock["시가"]),
                    high=int(stock["고가"]),
                    low=int(stock["저가"]),
                    close=int(stock["종가"]),
                    volume=int(stock["거래량"]),
                    amount=int(stock["거래대금"])
                )
                self.stockEntityRepository.save_entity(stockEntity)


