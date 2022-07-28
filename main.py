from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from controller.request import list_stocks_by_condition_request
from controller.request.list_stocks_by_condition_request import ListStocksByConditionRequest
from controller.response.list_stocks_by_condition_response import ListStocksByConditionResponse
from entity.data.condition import Condition
from service.stock_condition_service import StockConditionService

app = FastAPI()

stockConditionService = StockConditionService()


@app.get("/")
def back_test_stocks():
    return "hello world"


@app.get("/list_by_condition", response_model=ListStocksByConditionResponse)
def list_stocks_by_condition(condition: ListStocksByConditionRequest):
    condition_model = Condition(
        date=condition.date,
        volume_orders=condition.volume_orders,
        amount_orders=condition.amount_orders,
        changerate_orders=condition.changerate_orders,
        cci_orders=condition.cci_orders,
        psar_orders=condition.psar_orders,
        sigma_orders=condition.sigma_orders
    )
    res = stockConditionService.find_stocks_by_filter(condition_model)
    return ListStocksByConditionResponse(
        date=condition.date,
        codes=res
    )

# class StockController:
#     def __init__(self):
#         self.stockConditionService = StockConditionService()
#
#     @controller.get("/")
#     def back_test_stocks(self):
#         return "hello world"
#
#     @controller.get("/", response_model=ListStocksByConditionResponse)
#     def list_stocks_by_condition(self, condition: list_stocks_by_condition_request):
#         conditionModel = Condition(
#             date=condition.date,
#             volume_orders=condition.volume_orders,
#             amount_orders=condition.amount_orders,
#             changerate_orders=condition.chan,
#             cci_orders=condition.cci_orders,
#             psar_orders=condition.psar_orders,
#             sigma_orders=condition.sigma_orders
#         )
#         res = self.stockConditionService.findStocksByFilter(conditionModel)
#         return ListStocksByConditionResponse(
#             date=condition.date,
#             codes=res
#         )



