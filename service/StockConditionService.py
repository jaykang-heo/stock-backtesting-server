import datetime

from entity.data import Filter, VolumeOrder, AmountOrder, CciOrder, ChangeRateOrder, PsarOrder, SigmaOrder
from repository.StockEntityRepository import StockEntityRepository


class StockConditionService:
    def __init__(self):
        self.stockRepository = StockEntityRepository()

    def findStocksByFilter(self, filter: Filter):
        volumeOrderedStocks = []
        for volumeOrderFilter in filter.volumeOrders:
            volumeOrderedStock = self.stockRepository.findByVolumeOrder(
                filter.date,
                volumeOrderFilter.limit,
                volumeOrderFilter.ascending
            )
            for stock in volumeOrderedStock:
                volumeOrderedStocks.append(stock)

        amountOrderedStocks = []
        for amountOrderFilter in filter.amountOrders:
            amountOrderedStock = self.stockRepository.findByAmountOrder(
                filter.date,
                amountOrderFilter.limit,
                amountOrderFilter.ascending
            )
            for stock in amountOrderedStock:
                amountOrderedStocks.append(stock)

        changerateOrderedStocks = []
        for changeRateOrderFilter in filter.changeRateOrders:
            changerateOrderedStock = self.stockRepository.findByChnageRateOrder(
                filter.date,
                changeRateOrderFilter.limit,
                changeRateOrderFilter.ascending
            )
            for stock in changerateOrderedStock:
                changerateOrderedStocks.append(stock)

        temp1 = set([i[0] for i in volumeOrderedStocks])
        temp2 = set([i[0] for i in amountOrderedStocks])
        temp3 = set([i[0] for i in changerateOrderedStocks])

        codes = list(temp1 & temp2 & temp3)

        cciStocks = []
        for code in codes:
            for cciFilter in filter.cciOrders:
                cciStock = self.stockRepository.findByCci(
                    filter.date,
                    code,
                    cciFilter.period,
                    cciFilter.line
                )
                cciStocks.append(cciStock)

        sigmaStocks = []
        for code in codes[:1]:
            for sigmaFilter in filter.sigmaOrders:
                sigmaStock = self.stockRepository.findBySigma(
                    filter.date,
                    code,
                    sigmaFilter.period,
                    sigmaFilter.line
                )
                sigmaStocks.append(sigmaStock)

        psarStocks = []
        for code in codes:
            for psarFilter in filter.psarOrders:
                psarStock = self.stockRepository.findByParabolicUpper(
                    filter.date,
                    code,
                    psarFilter.acceleration,
                    psarFilter.maximum,
                    psarFilter.upper
                )
                psarStocks.append(psarStock)

        temp4 = set([i[0] for i in cciStocks if i is not None])
        # temp5 = [i[0] for i in sigmaStocks]
        # temp6 = [i[0] for i in psarStocks]

        res = temp1 & temp2 & temp3 & temp4

        return res

    def findStocksByCode(self, date, codes, volumeDescending):
        if volumeDescending:
            entities = self.stockRepository.findStocksByCodesAndOrderByVolumeDescending(date, codes)
            return [i[0] for i in entities]



