import datetime

from entity.data import condition
from entity.data.amount_order import AmountOrder
from entity.data.cci_order import CciOrder
from entity.data.changerate_order import ChangeRateOrder
from entity.data.condition import Condition
from entity.data.psar_order import PsarOrder
from entity.data.volume_order import VolumeOrder
from infra.fdr_service import FdrService
from infra.krx_service import KrxService
from repository.stock_entity_repository import StockEntityRepository
import talib

from service.utils import Utils


class StockConditionService:
    def __init__(self):
        self.stockRepository = StockEntityRepository()
        self.fdrService = FdrService()
        self.utils = Utils()

    def find_stocks_by_cci_filter(self, codes, cci_order: CciOrder):
        res = []
        for code in codes:
            cci_stock = self.stockRepository.find_by_cci(
                cci_order.date,
                code,
                cci_order.period,
                cci_order.line,
                cci_order.operator
            )
            if cci_stock:
                res.append(cci_stock[0])
        return res

    def find_stocks_by_code_volume_order(self, date, codes, volume_descending):
        if volume_descending:
            entities = self.stockRepository.find_stocks_by_codes_and_order_by_volume_descending(date, codes)
            return [i[0] for i in entities]

    def result_by_prices(self, first, second, third):
        pass

    def find_stocks_by_psar_filter(self, date, code, psar_order: PsarOrder):
        res = self.fdrService.find_df_stocks_by_code(code, date)
        psar_res = talib.SAR(
            high=res["High"],
            low=res["Low"],
            acceleration=psar_order.acceleration,
            maximum=psar_order.maximum
        )
        entity = self.utils.tupleToStockEntity(res[0])
        if entity.high >= psar_res.iloc[-1]:
            return res[0]

    def find_stocks_by_filter(self, condition_set: condition):
        volume_ordered_stocks = []
        if condition_set.volume_orders:
            for volumeOrderFilter in condition_set.volume_orders:
                volume_ordered_stock = self.stockRepository.find_by_volume_order(
                    condition_set.date,
                    volumeOrderFilter.limit,
                    volumeOrderFilter.ascending
                )
                for stock in volume_ordered_stock:
                    volume_ordered_stocks.append(stock)
        print(volume_ordered_stock)
        print("finished volume orders")

        amount_ordered_stocks = []
        if condition_set.amount_orders:
            for amountOrderFilter in condition_set.amount_orders:
                amount_ordered_stock = self.stockRepository.find_by_amount_order(
                    condition_set.date,
                    amountOrderFilter.limit,
                    amountOrderFilter.ascending
                )
                for stock in amount_ordered_stock:
                    amount_ordered_stocks.append(stock)
        print(amount_ordered_stock)
        print("finished amount orders")

        changerate_ordered_stocks = []
        if condition_set.changerate_orders:
            for changeRateOrderFilter in condition_set.changerate_orders:
                changerate_ordered_stock = self.stockRepository.find_by_changerate_order(
                    condition_set.date,
                    changeRateOrderFilter.limit,
                    changeRateOrderFilter.ascending
                )
                for stock in changerate_ordered_stock:
                    changerate_ordered_stocks.append(stock)
        print(changerate_ordered_stock)
        print("finished changerate orders")

        temp1 = set([i[0] for i in volume_ordered_stocks])
        temp2 = set([i[0] for i in amount_ordered_stocks])
        temp3 = set([i[0] for i in changerate_ordered_stocks])

        print(temp1)
        print("052220" in temp1)

        print(temp2)
        print("052220" in temp2)
        print(temp3)
        codes = list(temp1 & temp2 & temp3)
        print(codes)

        cci_stocks = []
        if condition_set.cci_orders:
            for code in codes:
                for cci_order in condition_set.cci_orders:
                    cci_stock = self.stockRepository.find_by_cci(
                        cci_order.date,
                        code,
                        cci_order.period,
                        cci_order.line,
                        cci_order.operator
                    )
                    cci_stocks.append(cci_stock)
        print("finished cci orders")

        temp4 = set([i[0] for i in cci_stocks if i is not None])

        if not codes:
            return set(temp4)
        else:
            return temp1 & temp2 & temp3 & temp4

