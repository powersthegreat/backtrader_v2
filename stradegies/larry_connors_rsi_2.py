# larry connors rsi 2 stradegy, rules include...
# 1. security must be above 200 day moving average to buy and below to sell
# 2. 2-period rsi must be between 0 and 10 to buy or between 90 and 100 to sell
# 3. recommended to buy and sell before the close rather than after
# 4. exit long positions on a move above the 5-day sma and exit short positions
#    on a move below the 5-day sma
# 5. no stops are recommended (but possibly use % of portfolio loss as stop)

# specifications
# 1. 200-period sma
# 2. 5-period sma
# 3. 2-period rsi
# 4. not that complicated

import time
import sys
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\stradegies\plotting')
import plot_stradegy

class Stradegy:
    def __init__(self, order_size):
        self.order_size = order_size

        # sma variables
        self.sma_200_period = 201
        self.sma_5_period = 6
        self.sma_200_queue = []
        self.sma_5_queue = []
        self.current_5_sma = None
        self.current_200_sma = None

        # rsi variables
        self.rsi_period = 2
        self.daily_gain_list = []
        self.daily_loss_list = []
        self.prev_close = None
        self.avg_gain_list = []
        self.avg_loss_list = []
        self.current_rsi = None
       
        self.stradegy_started = False
        self.current_state = "pass"
        self.test_plot = plot_stradegy.Plot_Stradegy()
   
    def move_sma_5(self, close):
        current_val = ((close) + sum(self.sma_5_queue)) / (self.sma_5_period)
        self.sma_5_queue.pop(0)
        self.sma_5_queue.append(close)
        return current_val

    def move_sma_200(self, close):
        current_val = ((close) + sum(self.sma_200_queue)) / (self.sma_200_period)
        self.sma_200_queue.pop(0)
        self.sma_5_queue.append(close)
        return current_val

    def move_rsi(self, close):
        daily_change = round((self.prev_close - close), 4)
        if len(self.daily_gain_list) < self.rsi_period:
            if daily_change > 0:
                self.daily_gain_list.append(daily_change)
                self.daily_loss_list.append(0)
            elif daily_change < 0:
                self.daily_loss_list.append(daily_change*(-1))
                self.daily_gain_list.append(0)
            else:
                self.daily_gain_list.append(0)
                self.daily_loss_list.append(0)
            self.avg_gain_list.append(0)
            self.avg_loss_list.append(0)
            return 0

        elif self.avg_gain_list[-1] == 0 and self.avg_loss_list[-1] == 0:
            if daily_change > 0:
                self.daily_gain_list.append(daily_change)
                self.daily_loss_list.append(0)
            elif daily_change < 0:
                self.daily_loss_list.append(daily_change*(-1))
                self.daily_gain_list.append(0)
            else:
                self.daily_gain_list.append(0)
                self.daily_loss_list.append(0)

            temp_gain_list = self.daily_gain_list[i-(self.rsi_period):i]
            temp_loss_list = self.daily_loss_list[i-(self.rsi_period):i]
            avg_gain_val = round(sum(temp_gain_list)/len(temp_gain_list), 4)
            avg_loss_val = round(sum(temp_loss_list)/len(temp_loss_list), 4)
            self.avg_gain_list.append(avg_gain_val)
            self.avg_loss_list.append(avg_loss_val)
            temp_gain_list = []
            temp_loss_list = []
            return 0

        else:
            if daily_change > 0:
                self.daily_gain_list.append(daily_change)
                self.daily_loss_list.append(0)
            elif daily_change < 0:
                self.daily_loss_list.append(daily_change*(-1))
                self.daily_gain_list.append(0)
            else:
                self.daily_gain_list.append(0)
                self.daily_loss_list.append(0)

            temp_gain_list = self.daily_gain_list[i-(self.rsi_period):i]
            temp_loss_list = self.daily_loss_list[i-(self.rsi_period):i]
            avg_gain_val = round(sum(temp_gain_list)/len(temp_gain_list), 4)
            avg_loss_val = round(sum(temp_loss_list)/len(temp_loss_list), 4)
            self.avg_gain_list.append(avg_gain_val)
            self.avg_loss_list.append(avg_loss_val)
            temp_gain_list = []
            temp_loss_list = []

            numerator_1 = (self.avg_gain_list[-2])*(self.rsi_period-1)
            numerator_2 = (numerator_1 + self.avg_gain_list[-1])/(self.rsi_period)
            denomerator_1 = (self.avg_loss_list[-2])*(self.rsi_period-1)
            denomerator_2 = (denomerator_1 + self.avg_loss_list[-1])/(self.rsi_period)
            try:
                current_val = round((numerator_2/denomerator_2), 4)
            except ZeroDivisionError:
                current_val = 0
            return current_val


    def logic(self, data):
        # first build up the sma queues
        close = float(data["close"])
        self.test_plot.append_close(close)

        if len(self.sma_200_queue) < (self.sma_200_period-1):
            self.sma_200_queue.append(close)

            if len(self.sma_5_queue) < (self.sma_5_period-1):
                self.sma_5_queue.append(close)
            else:
                self.current_5_sma = self.move_sma_5(close)
           
            if len(self.daily_gain_list) == 0 or len(self.daily_loss_list) == 0:
                self.daily_gain_list.append(0)
                self.daily_loss_list.append(0)
                self.avg_gain_list.append(0)
                self.avg_gain_list.append(0)
            else:
                self.current_rsi = self.move_rsi(close)
       
        self.current_200_sma = self.move_sma_200(close)
        self.current_5_sma = self.move_sma_5(close)
        self.current_rsi = self.move_rsi(close)
        print(self.current_200_sma)
        print(self.current_5_sma)
        print(self.current_rsi)

        self.prev_close = close