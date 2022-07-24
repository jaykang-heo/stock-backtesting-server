from entity.data import Filter, VolumeOrder, AmountOrder, CciOrder, ChangeRateOrder, PsarOrder, SigmaOrder
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

        changerateOrderedStocks = self.stockRepository.findByChnageRateOrder(
            filter.date,
            filter.changeRateOrder.limit,
            filter.changeRateOrder.ascending
        )

        cciStocks = self.stockRepository.findByCci(
            filter.date,
            filter.cciOrder.period,
            filter.cciOrder.line
        )
        print(cciStocks)

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


test = StockConditionService()
volumeOrder = VolumeOrder.VolumeOrder(10, False)
amountOrder = AmountOrder.AmountOrder(10, False)
changeRateOrder = ChangeRateOrder.ChangeRateOrder(10, False)
cciOrder = CciOrder.CciOrder(6000, 100)
psarOrder = PsarOrder.PsarOrder(0.0000002, 0.0000002, True)
sigmaOrder = SigmaOrder.SigmaOrder(20, 200)
res = test.findStocksByFilter(
    Filter.Filter(
        20220722,
        volumeOrder=volumeOrder,
        amountOrder=amountOrder,
        changeRateOrder=changeRateOrder,
        cciOrder=cciOrder,
        psarOrder=psarOrder,
        sigmaOrder=sigmaOrder
    )
)
