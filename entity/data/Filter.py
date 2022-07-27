from typing import List

from entity.data import VolumeOrder, SigmaOrder, PsarOrder, ChangeRateOrder, CciOrder, AmountOrder


class Filter:
    def __init__(
            self,
            date,
            volumeOrders,
            amountOrders,
            cciOrders,
            changeRateOrders,
            psarOrders,
            sigmaOrders
    ):
        self.date = date
        self.volumeOrders = volumeOrders
        self.amountOrders = amountOrders
        self.sigmaOrders = sigmaOrders
        self.psarOrders = psarOrders
        self.changeRateOrders = changeRateOrders
        self.cciOrders = cciOrders
