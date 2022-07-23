from entity.data import Filter
from repository.StockEntityRepository import StockEntityRepository


class StockConditionService:
    def __init__(self):
        self.stockRepository = StockEntityRepository()

    def findStocksByFilter(self, filter: Filter):
        volumeOrderedStocks = self.stockRepository.findByVolumeOrder(
            filter.date,
            filter.volumeOrder.limit,
            filter.volumeOrder.ascending
        )

        amountOrderedStocks = self.stockRepository.findByAmountOrder(
            filter.date,
            filter.amountOrder.limit,
            filter.amountOrder.ascending
        )

        # changerateOrderedStocks = self.stockRepository.findByChnageRateOrder(
        #     filter.date,
        #     filter.changeRateOrder.limit,
        #     filter.changeRateOrder.ascending
        # )
        #
        # cciStocks = self.stockRepository.findByCci(
        #     filter.date,
        #     filter.cciOrder.period,
        #     filter.cciOrder.line
        # )
        #
        # sigmaStocks = self.stockRepository.findBySigma(
        #     filter.date,
        #     filter.sigmaOrder.period,
        #     filter.sigmaOrder.line
        # )
        #
        # psarStocks = self.stockRepository.findByParabolic(
        #     filter.date,
        #     filter.psarOrder.acceleration,
        #     filter.psarOrder.maximum,
        #     filter.psarOrder.upper
        # )

        return volumeOrderedStocks

