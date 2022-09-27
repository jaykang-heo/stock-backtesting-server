import FinanceDataReader as fdr

from entity.stock_entity import StockEntity


class FdrService:
    def __init__(self):
        self.fdr = fdr

    def find_stocks_by_code(self, code):
        stocks = self.fdr.DataReader(symbol=code)
        stock_entities = []
        for index, stock in stocks.iterrows():
            stock = StockEntity(
                code=code,
                stock_type="",
                changerate=float(stock["Change"]),
                date=index,
                open=int(stock["Open"]),
                high=int(stock["High"]),
                low=int(stock["Low"]),
                close=int(stock["Close"]),
                volume=int(stock["Volume"]),
                amount=None
            )
            stock_entities.append(stock)
        return stock_entities

    def find_df_stocks_by_code(self, code, date):
        res = self.fdr.DataReader(symbol=code, end=date)
        return self.fdr.DataReader(symbol=code, end=date)
