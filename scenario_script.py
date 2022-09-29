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
        from_date=20220929,
        to_date=20220929
    )


# list stocks by condition filters
def searchStock():
    krxService = KrxService()
    dates = krxService.get_valid_business_days(20200207, 20220921)
    # dates = krxService.get_valid_business_days(20220919, 20220921)
    service = StockConditionService()
    for idx in range(len(dates))[1:]:
        f = open("stocks.txt", "w")
        date = dates[idx]
        try:
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
                        ),
                        CciOrder(
                            date=dates[idx-1],
                            period=60,
                            line=100,
                            operator=False
                        )
                    ],
                )
            )
            if res:
                print(date, res)
            else:
                print("                       ", date, res)
            f.write("{0}, {1} \n".format(date, res))
            f.close()
        except:
            # print(date, "error")
            f.write("{0}, error \n".format(date))
            f.close()
            pass


searchStock()
