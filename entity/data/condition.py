from typing import List

from entity.data import volume_order, sigma_order, psar_order, changerate_order, cci_order, amount_order


class Condition:
    def __init__(
            self,
            date,
            volume_orders,
            amount_orders,
            cci_orders,
            changerate_orders,
            psar_orders,
            sigma_orders
    ):
        self.date = date
        self.volume_orders = volume_orders
        self.amount_orders = amount_orders
        self.sigma_orders = sigma_orders
        self.psar_orders = psar_orders
        self.change_rate_orders = changerate_orders
        self.cci_orders = cci_orders
