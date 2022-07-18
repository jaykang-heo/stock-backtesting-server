from entity.data import Filter
from entity.data import VolumeOrder
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
        return volumeOrderedStocks

