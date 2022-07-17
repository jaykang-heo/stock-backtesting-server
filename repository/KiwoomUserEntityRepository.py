import asyncio

from koapy import KiwoomOpenApiPlusEntrypoint
from koapy.utils.data import KrxHistoricalDailyPriceDataDownloader
import pandas as pd
from koapy.utils.data import KrxHistoricalDailyPriceDataLoader
import datetime
import json
from koapy import KiwoomOpenApiPlusEntrypoint
import time
from os import listdir
import os.path
from os.path import isfile, join


def getOneStockFromKiwoom(code):
    with KiwoomOpenApiPlusEntrypoint() as context:
        # 이벤트를 알아서 처리하고 결과물만 제공하는 상위 함수 사용 예시
        code = "005930"
        info = context.GetStockBasicInfoAsDict(code)
        print(info)
        price = info["현재가"]
        print(price)