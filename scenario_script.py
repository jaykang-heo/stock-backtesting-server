from entity.data.amount_order import AmountOrder
from entity.data.cci_order import CciOrder
from entity.data.changerate_order import ChangeRateOrder
from entity.data.condition import Condition
from entity.data.psar_order import PsarOrder
from entity.data.volume_order import VolumeOrder
from infra.krx_service import KrxService
from service.stock_condition_service import StockConditionService
from service.stock_service import StockService


# save all stock data from today until first day of the code
def downloadStockData():
    test = StockService()
    test.download_krx_data(
        from_date=20130327,
        to_date=20220928
    )


# list stocks by condition filters
def searchStock():
    krxService = KrxService()
    dates = krxService.get_valid_business_days(20130327, 20220921)
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
                        date=date,
                        period=60,
                        line=300,
                        operator=True
                    )
                ],
            )
        )

        if len(res):
            print(date, res)


downloadStockData()
