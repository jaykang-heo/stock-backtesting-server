import datetime

from entity.data import condition
from entity.data.amount_order import AmountOrder
from entity.data.cci_order import CciOrder
from entity.data.changerate_order import ChangeRateOrder
from entity.data.condition import Condition
from entity.data.volume_order import VolumeOrder
from infra.krx_service import KrxService
from repository.stock_entity_repository import StockEntityRepository


class StockConditionService:
    def __init__(self):
        self.stockRepository = StockEntityRepository()

    def find_stocks_by_filter(self, condition_set: condition):
        volume_ordered_stocks = []
        if condition_set.volume_orders:
            for volumeOrderFilter in condition_set.volume_orders:
                volume_ordered_stock =  self.stockRepository.find_by_volume_order(
                    condition_set.date,
                    volumeOrderFilter.limit,
                    volumeOrderFilter.ascending
                )
                for stock in volume_ordered_stock:
                    volume_ordered_stocks.append(stock)
        print("finished volume orders")

        amount_ordered_stocks = []
        if condition_set.amount_orders:
            for amountOrderFilter in condition_set.amount_orders:
                amount_ordered_stock =  self.stockRepository.find_by_amount_order(
                    condition_set.date,
                    amountOrderFilter.limit,
                    amountOrderFilter.ascending
                )
                for stock in amount_ordered_stock:
                    amount_ordered_stocks.append(stock)
        print("finished amount orders")

        changerate_ordered_stocks = []
        if condition_set.changerate_orders:
            for changeRateOrderFilter in condition_set.changerate_orders:
                changerate_ordered_stock =  self.stockRepository.find_by_changerate_order(
                    condition_set.date,
                    changeRateOrderFilter.limit,
                    changeRateOrderFilter.ascending
                )
                for stock in changerate_ordered_stock:
                    changerate_ordered_stocks.append(stock)
        print("finished changerate orders")

        temp1 = set([i[0] for i in volume_ordered_stocks])
        temp2 = set([i[0] for i in amount_ordered_stocks])
        temp3 = set([i[0] for i in changerate_ordered_stocks])

        codes = list(temp1 & temp2 & temp3)

        cci_stocks = []
        if condition_set.cci_orders:
            for code in codes:
                for cci_order in condition_set.cci_orders:
                    cci_stock = self.stockRepository.find_by_cci(
                        condition_set.date,
                        code,
                        cci_order.period,
                        cci_order.line
                    )
                    cci_stocks.append(cci_stock)

        print("finished cci orders")

        sigma_stocks = []
        if condition_set.sigma_orders:
            for code in codes[:1]:
                for sigmaFilter in condition_set.sigma_orders:
                    sigma_stock = self.stockRepository.find_by_sigma(
                        condition_set.date,
                        code,
                        sigmaFilter.period,
                        sigmaFilter.line
                    )
                    sigma_stocks.append(sigma_stock)
        print("finished sigma orders")

        psar_stocks = []
        if condition_set.psar_orders:
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
        print("finished psar orders")

        temp4 = set([i[0] for i in cci_stocks if i is not None])
        # temp5 = [i[0] for i in sigma_stocks]
        # temp6 = [i[0] for i in psar_stocks]

        res = temp1 & temp2 & temp3 & temp4

        return res

    def find_stocks_by_code_volume_order(self, date, codes, volume_descending):
        if volume_descending:
            entities = self.stockRepository.find_stocks_by_codes_and_order_by_volume_descending(date, codes)
            return [i[0] for i in entities]


krxService = KrxService()
dates = krxService.get_valid_business_days(20100101, 20220727)
service = StockConditionService()
for date in dates:
    res = service.find_stocks_by_filter(
        Condition(
            date=date,
            volume_orders=[
                VolumeOrder(
                    limit=200,
                    ascending=False
                )
            ],
            amount_orders=[
                AmountOrder(
                    limit=200,
                    ascending=False
                )
            ],
            changerate_orders=[
                ChangeRateOrder(
                    limit=100,
                    ascending=False
                )
            ],
            cci_orders=[
                CciOrder(
                    period=60,
                    line=100
                )
            ],
        )
    )
    print(res)
    print("------------------------")