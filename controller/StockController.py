from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from controller.response.ListStocksResponse import ListStocksResponse
from entity.data.Filter import Filter
from service.StockConditionService import StockConditionService

app = FastAPI()


class StockController:
    def __init__(self):
        self.stockConditionService = StockConditionService()

    @app.get("/")
    def back_test_stocks(self):
        pass

    @app.get("/", response_model=ListStocksResponse)
    def list_stocks(self, stock_filter: Filter):
        return self.stockConditionService.findStocksByFilter(filter)



