# stradegy class:
# - takes in data feed from operate
# - returns order to operate
# - operate will pass order to other classes
# - each stradegy needs to have logic to not 'overlap' buy/sell orders
# - aka. keep it simple for now
# - first example will be 10 period SMA crossover

# specifications
# - period can be altered to change moving average range
# - prev_sma can be altered to change how far back is looked when
#   determining a crossover
# - 


import time
import sys
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\stradegies\plotting')
import plot_stradegy

class Stradegy:
    def __init__(self, order_size):
        self.order_size = order_size
        self.period = 10
        self.sma_queue = []
        self.stradegy_started = False
        self.prev_sma_value = None
        self.current_state = "pass"
        self.test_plot = plot_stradegy.Plot_Stradegy()

    def logic(self, data):
        #formula = (current_close + prev. x closes)/period
        #remember that method is called individualy everytime
        #a new data feed is ready, everything needs to be stored
        #as memember variable

        # sma_current = (float(data["close"]) + sum(sma_queue))/period
        close = float(data["close"])
        self.test_plot.append_close(close)

        #if sma queue not filled yet
        if len(self.sma_queue) < (self.period-1):
            self.sma_queue.append(close)
            print(f"close: {close}, sma: building queue-a, order: 'pass'")
            self.test_plot.append_stradegy(close)
            time.sleep(.15)
            return "pass"
        #loading prev_sma_value
        if self.prev_sma_value == None:
            self.prev_sma_value = ((close) + sum(self.sma_queue))/self.period
            self.sma_queue.pop(0)
            self.sma_queue.append(close)
            print(f"close: {close}, sma: building queue-b, order: 'pass'")
            self.test_plot.append_stradegy(close)
            time.sleep(.15)
            return "pass"
        
        current_sma = ((close) + sum(self.sma_queue))/self.period
        self.test_plot.append_stradegy(current_sma)

        #starting stradegy
        if self.stradegy_started == False:
            print(f"current state: {self.current_state}")
            if self.prev_sma_value >= close and current_sma < close:
                #starting long when sma goes from above close to below
                #reversely engineered than if stradegy started was true
                self.current_state = "buy"
                self.stradegy_started = True
                self.sma_queue.pop(0)
                self.sma_queue.append(close)
                self.prev_sma_value = current_sma
                print("stradegy started long")
                print(f"close: {close}, rev sma: {self.prev_sma_value}, sma: {current_sma}, order: 'buy'")
                time.sleep(.15)
                return "buy"
            elif self.prev_sma_value <= close and current_sma > close:
                #starting short when sma goes from under close to above
                #reversely engineered than if stradegy started was true
                self.current_state = "sell"
                self.stradegy_started = True
                self.sma_queue.pop(0)
                self.sma_queue.append(close)
                self.prev_sma_value = current_sma
                print("stradegy start short")
                print(f"close: {close}, rev sma: {self.prev_sma_value}, sma: {current_sma}, order: 'sell'")
                time.sleep(.15)
                return "sell"
            else:
                self.sma_queue.pop(0)
                self.sma_queue.append(close)
                self.prev_sma_value = current_sma
                print(f"close: {close}, prev sma: {self.prev_sma_value}, sma: {current_sma}, order: 'pass'")
                time.sleep(.15)
                return "pass"
        
        #running started stradegy
        else:
            print(f'current state: {self.current_state}')
            if self.current_state == "buy" and close < current_sma:
                #selling out when close crosses below sma
                self.current_state = "sell"
                print(f"close: {close}, sma: {current_sma}, order: 'sell'")
                self.sma_queue.pop(0)
                self.sma_queue.append(close)
                self.prev_sma_value = current_sma
                time.sleep(.15)
                return "sell"
                pass
            elif self.current_state == "buy" and close >= current_sma:
                #holding
                print(f"close: {close}, sma: {current_sma}, order: 'pass'")
                self.sma_queue.pop(0)
                self.sma_queue.append(close)
                self.prev_sma_value = current_sma
                time.sleep(.15)
                return "pass"
            elif self.current_state == "sell" and close > current_sma:
                #buying back when close crosses above sma
                self.current_state = "buy"
                print(f"close: {close}, sma: {current_sma}, order: 'buy'")
                self.sma_queue.pop(0)
                self.sma_queue.append(close)
                self.prev_sma_value = current_sma
                time.sleep(.15)
                return "buy"
            elif self.current_state == "sell" and close <= current_sma:
                #holding
                print(f"close: {close}, sma: {current_sma}, order: 'pass'")
                self.sma_queue.pop(0)
                self.sma_queue.append(close)
                self.prev_sma_value = current_sma
                time.sleep(.15)
                return "pass"
            else:
                raise RuntimeError("Something went wrong in stradegy!")

    def plot_stradegy(self):
        self.test_plot.plot()

        
        
        
        
        




    
        
        
        
        
