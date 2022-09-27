from entity.stock_entity import StockEntity
from infra.fdr_service import FdrService
from repository.stock_entity_repository import StockEntityRepository
from infra.krx_service import KrxService
from service.utils import Utils
import datetime


class StockService:
    def __init__(self):
        self.stockEntityRepository = StockEntityRepository()
        # disable table format
        # self.stockEntityRepository.delete_all()
        self.krxService = KrxService()
        self.utils = Utils()
        self.fdrService = FdrService()

    def download_krx_data(self, from_date=None, to_date=None):
        today = datetime.date.today().strftime('%Y%m%d')
        if not from_date:
            from_date = 19950101
        if not to_date:
            to_date = today
        valid_dates = self.krxService.get_valid_business_days(from_date=from_date, to_date=to_date)
        for date in valid_dates:
            stocks = self.krxService.find_stocks_by_code(date)
            print(date, len(stocks))
            for index, stock in stocks.iterrows():
                stock_entity = StockEntity(
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
                self.stockEntityRepository.save_entity("PYKRX", stock_entity)

    def download_fdr_data(self):
        codes = self.krxService.get_stock_codes()
        print(codes)
        for idx, code in enumerate(codes):
            stocks = self.fdrService.find_stocks_by_code(code)
            print(len(codes), idx, len(stocks))
            for i in stocks:
                self.stockEntityRepository.save_entity("FDR", i)



test = StockService()
test.download_fdr_data()
