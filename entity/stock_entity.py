class StockEntity(object):
    # TODO: get accurate quarter and year profit
    def __init__(self, code, stock_type, date, changerate, open, high, low, close, volume, amount):
        # 종목코드
        self.code = code
        # 주식 종류 i.e KOSDAQ, KOSPI, ETF, ...
        self.stockType = stock_type
        # 일봉 일자
        self.date = date
        self.changerate = changerate
        # 시가
        self.open = open
        # 고가
        self.high = high
        # 저가
        self.low = low
        # 종가
        self.close = close
        # 거래량
        self.volume = volume
        # 거래대금
        self.amount = amount

    def toDict(self):
        return {
            'code': self.code,
            'stockType': self.stockType,
            'date': self.date,
            'changeRate': self.changerate,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volume': self.volume,
            'amount': self.amount
        }


