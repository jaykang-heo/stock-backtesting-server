import talib

from repository.StockEntityRepository import StockEntityRepository


class StockConditionService:
    def __int__(self):
        self.stockRepository = StockEntityRepository()
        pass

    def __isCCIAboveLine(self, duration, stocks, line):
        pass

    def __isSigmaAboveLine(self, duration, stocks, line):
        pass

    def __isYesterdayChangeRateUnderTen(self, stocks):
        res = []
        prev = stocks[0]
        for stock in stocks[1:]:
            if 0 < prev < 10:
                res.append(stock)
        return res

    def __isPsarUpBreak(self):
        pass

    def __findTopAmount(self, num):
        return self.stockRepository.findAllStocksByAmountDescending(num)

    def __findTopVolume(self, num):
        return self.stockRepository.findAllStocksByVolumeDescending(num)

    def __findTopChangeRate(self, num):
        return self.stockRepository.findAllStocksByChangeRateDescending(num)

    def __isChangeRatePositive(self, stocks):
        res = []
        for stock in stocks:
            if stock.changeRate > 0:
                res.append(stock)
        return res

    def closeBuyTooMuchCondition(self):
        topChangeRateStocks = self.__findTopChangeRate(100)
        topVolumeStocks = self.__findTopVolume(200)
        topAmountStocks = self.__findTopAmount(200)
        cciStocks = self.__isCCIAboveLine()
        cciStocks = self.__isCCIAboveLine()
        sigmasStocks = self.__isSigmaAboveLine()
        sigmasStocks = self.__isSigmaAboveLine()
        underStocks = self.__isYesterdayChangeRateUnderTen()
        psarStocks = self.__isPsarUpBreak()
        positiveStocks = self.__isChangeRatePositive()

        pass