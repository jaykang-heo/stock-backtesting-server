import datetime

from entity.data import condition
from repository.stock_entity_repository import StockEntityRepository


class StockConditionService:
    def __init__(self):
        self.stockRepository = StockEntityRepository()

    def find_stocks_by_filter(self, condition_set: condition):
        volume_ordered_stocks = []
        for volumeOrderFilter in condition_set.volume_orders:
            volume_ordered_stock = self.stockRepository.find_by_volume_order(
                condition_set.date,
                volumeOrderFilter.limit,
                volumeOrderFilter.ascending
            )
            for stock in volume_ordered_stock:
                volume_ordered_stocks.append(stock)

        amount_ordered_stocks = []
        for amountOrderFilter in condition_set.amount_orders:
            amount_ordered_stock = self.stockRepository.find_by_amount_order(
                condition_set.date,
                amountOrderFilter.limit,
                amountOrderFilter.ascending
            )
            for stock in amount_ordered_stock:
                amount_ordered_stocks.append(stock)

        changerate_ordered_stocks = []
        for changeRateOrderFilter in condition_set.changerate_orders:
            changerate_ordered_stock = self.stockRepository.find_by_changerate_order(
                condition_set.date,
                changeRateOrderFilter.limit,
                changeRateOrderFilter.ascending
            )
            for stock in changerate_ordered_stock:
                changerate_ordered_stocks.append(stock)

        temp1 = set([i[0] for i in volume_ordered_stocks])
        temp2 = set([i[0] for i in amount_ordered_stocks])
        temp3 = set([i[0] for i in changerate_ordered_stocks])

        codes = list(temp1 & temp2 & temp3)

        cci_stocks = []
        for code in codes:
            for cci_order in condition_set.cci_orders:
                cci_stock = self.stockRepository.find_by_cci(
                    condition_set.date,
                    code,
                    cci_order.period,
                    cci_order.line
                )
                cci_stocks.append(cci_stock)

        sigma_stocks = []
        for code in codes[:1]:
            for sigmaFilter in condition_set.sigma_orders:
                sigma_stock = self.stockRepository.find_by_sigma(
                    condition_set.date,
                    code,
                    sigmaFilter.period,
                    sigmaFilter.line
                )
                sigma_stocks.append(sigma_stock)

        psar_stocks = []
        for code in codes:
            for psarFilter in condition_set.psar_orders:
                psar_stock = self.stockRepository.find_by_psar_upper(
                    condition_set.date,
                    code,
                    psarFilter.acceleration,
                    psarFilter.maximum,
                    psarFilter.upper
                )
                psar_stocks.append(psar_stock)

        temp4 = set([i[0] for i in cci_stocks if i is not None])
        # temp5 = [i[0] for i in sigma_stocks]
        # temp6 = [i[0] for i in psar_stocks]

        res = temp1 & temp2 & temp3 & temp4

        return res

    def find_stocks_by_code_volume_order(self, date, codes, volume_descending):
        if volume_descending:
            entities = self.stockRepository.find_stocks_by_codes_and_order_by_volume_descending(date, codes)
            return [i[0] for i in entities]



