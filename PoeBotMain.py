import time
import cmd

import TradeController

items = {"tabula_rasa": 10,
         "enlighten_2": 29,
         "enlighten_3": 30}

# perandus blazon
# watcher's eye with wraith mod
# the pariah
# darkscorn

trade_controller = TradeController.TradeController(items)


class PoeBot(cmd.Cmd):
    def __init__(self):
        super().__init__()
        print("poe bot starting")
        self.check_prices()

    def check_prices(self):
        while True:
            print("price checking")
            for item, price in items.items():
                trade_controller.check_price(item, price)
            time.sleep(30)
            # check prices


if __name__ == "__main__":
    PoeBot().cmdloop()
