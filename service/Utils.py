import datetime
import pandas as pd

from entity.StockEntity import StockEntity


class Utils:
    def tupleToStockEntity(self, tuple):
        return StockEntity(
            code=tuple[0],
            stockType=tuple[1],
            date=tuple[2],
            changeRate=tuple[3],
            open=tuple[4],
            high=int(tuple[5]),
            low=int(tuple[6]),
            close=int(tuple[7]),
            volume=int(tuple[8]),
            amount=int(tuple[9])
        )

    def getYearDates(self, date=None):
        if not date:
            date = datetime.date.today()
        sdate = datetime.date(2022, 1, 1)  # start date
        edate = datetime.date(date.year, date.month, date.day)
        res = pd.date_range(start=sdate, end=edate).strftime('%Y%m%d').tolist()
        # res = pd.date_range(start=sdate, end=sdate, freq="B").strftime('%Y%m%d').tolist()
        return res
