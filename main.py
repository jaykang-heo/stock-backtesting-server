from fastapi import FastAPI

from controller.request.list_stocks_by_condition_request import ListStocksByConditionRequest
from controller.response.list_stocks_by_condition_response import ListStocksByConditionResponse
from entity.data.condition import Condition
from service.stock_condition_service import StockConditionService

app = FastAPI()

stockConditionService = StockConditionService()


@app.get("/")
async def back_test_stocks():
    return "hello world"


@app.post("/list_by_condition", response_model=ListStocksByConditionResponse)
async def list_stocks_by_condition(condition: ListStocksByConditionRequest):
    print("request received")
    condition_model = Condition(
        date=condition.date,
        volume_orders=condition.volume_orders,
        amount_orders=condition.amount_orders,
        changerate_orders=condition.changerate_orders,
        cci_orders=condition.cci_orders,
        psar_orders=condition.psar_orders,
        sigma_orders=condition.sigma_orders
    )
    res = await stockConditionService.find_stocks_by_filter(condition_model)
    print("request finished, returning")
    return ListStocksByConditionResponse(
        date=condition.date,
        codes=res
    )


