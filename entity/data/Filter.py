from entity.data import VolumeOrder, SigmaOrder, PsarOrder, ChangeRateOrder, CciOrder, AmountOrder


class Filter:
    def __init__(
            self,
            date,
            volumeOrder: VolumeOrder,
            amountOrder: AmountOrder,
            cciOrder: CciOrder,
            changeRateOrder: ChangeRateOrder,
            psarOrder: PsarOrder,
            sigmaOrder: SigmaOrder
    ):
        self.date = date
        self.volumeOrder = volumeOrder
        self.sigmaOrder = sigmaOrder
        self.psarOrder = psarOrder
        self.changeRateOrder = changeRateOrder
        self.cciOrder = cciOrder
