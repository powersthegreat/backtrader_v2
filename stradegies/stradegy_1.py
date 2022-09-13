# stradegy class:
# - takes in data feed from operate
# - returns order to operate
# - operate will pass order to other classes
# - each stradegy needs to have logic to not 'overlap' buy/sell orders
# - aka. keep it simple for now
# - first example will be 10 period SMA crossover

class Stradegy:
    def __init__(self, order_size):
        self.order_size = order_size
        self.current_order = "pass"
        self.period = 10
        self.period_queue = []

    def logic(self, data):
        close = float(data["close"])
        #fill up the period queue
        while len(self.period_queue) != self.period:
            self.period_queue.append(close)
        
        current_sma = float(sum(self.period_queue)/self.period)

        #once full then 6 cases
        if self.current_order == "pass" and close > current_sma:
            self.period_queue.pop(-1)
            self.period_queue.insert(0, close)
            print("buy - current order:" + self.current_order)
            return "buy"

        elif self.current_order == "pass" and close < current_sma:
            self.period_queue.pop(-1)
            self.period_queue.insert(0, close)
            print("sell - current order:" + self.current_order)
            return "sell"

        elif self.current_order == "buy" and close > current_sma:
            self.period_queue.pop(-1)
            self.period_queue.insert(0, close)
            return "pass"

        elif self.current_order == "buy" and close < current_sma:
            self.period_queue.pop(-1)
            self.period_queue.insert(0, close)
            print("sell - current order:" + self.current_order)
            return "sell"

        elif self.current_order == "sell" and close > current_sma:
            self.period_queue.pop(-1)
            self.period_queue.insert(0, close)
            print("buy - current order:" + self.current_order)
            return "buy"

        elif self.current_order == "sell" and close < current_sma:
            self.period_queue.pop(-1)
            self.period_queue.insert(0, close)
            return "pass"

        else:
            raise RuntimeError("Cases failed...")
        
        
