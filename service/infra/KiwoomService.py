from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import QApplication
import sys
import pykiwoom
from pykiwoom.kiwoom import *


class KiwoomService:
    def __init__(self, init):
        if init:
            self.kiwoom = Kiwoom()
            self.kiwoom.CommConnect(block=True)

    def getStocksFromCondition(self):
        pass

    def getKospiCodes(self):
        return self.kiwoom.GetCodeListByMarket('0')

    def getKosdaqCodes(self):
        return self.kiwoom.GetCodeListByMarket('10')

    def findStockByCode(self, code, date):
        df_list = []
        tr = "opt10081"
        df_firstblock = self.kiwoom.block_request(
            tr,
            종목코드=code,
            기준일자=date,
            수정주가구분=1,
            output="주식일봉차트조회",
            next=0
        )
        df_list.append(df_firstblock)
        print('데이터 수집 시작.. ({}~)'.format(df_firstblock.loc[0, '일자']))
        print('데이터 수집 중.. (~{})'.format(df_firstblock.loc[len(df_firstblock) - 1, '일자']))

        # Too many data
        # while self.kiwoom.tr_remained:
        #     df_remainblock = self.kiwoom.block_request(
        #         tr,
        #         종목코드=code,
        #         기준일자=date,
        #         수정주가구분=1,
        #         output="주식일봉차트조회",
        #         next=2
        #     )
        #     df_list.append(df_remainblock)
        #     time.sleep(1)
        #     print('데이터 수집 중.. (~{})'.format(df_remainblock.loc[len(df_remainblock) - 1, '일자']))
        #     if not self.kiwoom.tr_remained:
        #         print('데이터 수집 완료')
        df_all = pd.concat(df_list)
        df_all.reset_index(drop=True, inplace=True)
        return df_all


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = KiwoomService()
    res = test.findStockByCode("005930", "20220426")
    print(res)

