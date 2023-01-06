# trys to reverse big losses by watching for previous quick period
# volume increases


import time
import sys
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\stradegies\plotting')
import plot_stradegy
from datetime import datetime

class Stradegy:
    def __init__(self, order_size, show_plot, sim_name):
        # main variables
        self.order_size = order_size
        self.show_plot = show_plot
        self.sim_name = sim_name
        self.stradegy_started = False
        self.position = None
        self.current_state = "pass"
        self.test_plot = plot_stradegy.Plot_Stradegy(show_plot, sim_name)
        self.counter = 0

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
        self.avg_gain_list = []
        self.avg_loss_list = []
        self.current_rsi = None

        self.rsi_period_2 = 10
        self.daily_gain_list_2 = []
        self.daily_loss_list_2 = []
        self.avg_gain_list_2 = []
        self.avg_loss_list_2 = []
        self.current_rsi_2 = None


        # prev variables
        self.prev_close = None
        self.prev_volume = None
   
    def move_sma_5(self, close):
        current_val = ((close) + sum(self.sma_5_queue)) / (self.sma_5_period)
        self.sma_5_queue.pop(0)
        self.sma_5_queue.append(close)
        return current_val

    def move_sma_200(self, close):
        current_val = ((close) + sum(self.sma_200_queue)) / (self.sma_200_period)
        self.sma_200_queue.pop(0)
        self.sma_200_queue.append(close)
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

            temp_gain_list = self.daily_gain_list[(-1)-(self.rsi_period):(-1)]
            temp_loss_list = self.daily_loss_list[(-1)-(self.rsi_period):(-1)]
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

            temp_gain_list = self.daily_gain_list[(-1)-(self.rsi_period):(-1)]
            temp_loss_list = self.daily_loss_list[(-1)-(self.rsi_period):(-1)]
            avg_gain_val = round(sum(temp_gain_list)/len(temp_gain_list), 4)
            avg_loss_val = round(sum(temp_loss_list)/len(temp_loss_list), 4)
            self.avg_gain_list.append(avg_gain_val)
            self.avg_loss_list.append(avg_loss_val)
            temp_gain_list = []
            temp_loss_list = []

            numerator_1 = (self.avg_gain_list[-2])*(self.rsi_period-1) + self.avg_gain_list[-1]
            denomerator_1 = (self.avg_loss_list[-2])*(self.rsi_period-1) + self.avg_loss_list[-1]
            try:
                val_1 = round((numerator_1/denomerator_1), 4)
            except ZeroDivisionError:
                val_1 = 0
            current_rsi = 100 - (100 / (1 + val_1))
            return current_rsi

    def move_rsi_2(self, close):
        daily_change = round((self.prev_close - close), 4)
        if len(self.daily_gain_list_2) < self.rsi_period_2:
            if daily_change > 0:
                self.daily_gain_list_2.append(daily_change)
                self.daily_loss_list_2.append(0)
            elif daily_change < 0:
                self.daily_loss_list_2.append(daily_change*(-1))
                self.daily_gain_list_2.append(0)
            else:
                self.daily_gain_list_2.append(0)
                self.daily_loss_list_2.append(0)
            self.avg_gain_list_2.append(0)
            self.avg_loss_list_2.append(0)
            return 0

        elif self.avg_gain_list_2[-1] == 0 and self.avg_loss_list_2[-1] == 0:
            if daily_change > 0:
                self.daily_gain_list_2.append(daily_change)
                self.daily_loss_list_2.append(0)
            elif daily_change < 0:
                self.daily_loss_list_2.append(daily_change*(-1))
                self.daily_gain_list_2.append(0)
            else:
                self.daily_gain_list_2.append(0)
                self.daily_loss_list_2.append(0)

            temp_gain_list = self.daily_gain_list_2[(-1)-(self.rsi_period_2):(-1)]
            temp_loss_list = self.daily_loss_list_2[(-1)-(self.rsi_period_2):(-1)]
            avg_gain_val = round(sum(temp_gain_list)/len(temp_gain_list), 4)
            avg_loss_val = round(sum(temp_loss_list)/len(temp_loss_list), 4)
            self.avg_gain_list_2.append(avg_gain_val)
            self.avg_loss_list_2.append(avg_loss_val)
            temp_gain_list = []
            temp_loss_list = []
            return 0

        else:
            if daily_change > 0:
                self.daily_gain_list_2.append(daily_change)
                self.daily_loss_list_2.append(0)
            elif daily_change < 0:
                self.daily_loss_list_2.append(daily_change*(-1))
                self.daily_gain_list_2.append(0)
            else:
                self.daily_gain_list_2.append(0)
                self.daily_loss_list_2.append(0)

            temp_gain_list = self.daily_gain_list_2[(-1)-(self.rsi_period_2):(-1)]
            temp_loss_list = self.daily_loss_list_2[(-1)-(self.rsi_period_2):(-1)]
            avg_gain_val = round(sum(temp_gain_list)/len(temp_gain_list), 4)
            avg_loss_val = round(sum(temp_loss_list)/len(temp_loss_list), 4)
            self.avg_gain_list_2.append(avg_gain_val)
            self.avg_loss_list_2.append(avg_loss_val)
            temp_gain_list = []
            temp_loss_list = []

            numerator_1 = (self.avg_gain_list_2[-2])*(self.rsi_period_2-1) + self.avg_gain_list_2[-1]
            denomerator_1 = (self.avg_loss_list_2[-2])*(self.rsi_period_2-1) + self.avg_loss_list_2[-1]
            try:
                val_1 = round((numerator_1/denomerator_1), 4)
            except ZeroDivisionError:
                val_1 = 0
            current_rsi = 100 - (100 / (1 + val_1))
            return current_rsi


    def logic(self, data):
        # getting close from data feed and sending to plotting class
        close = float(data["close"])
        volume = float(data["volume"])
        self.test_plot.append_close(close)
        self.counter += 1
        # print(self.counter)

        # first building up 200 sma, 5 sma, and 2 rsi indicators
        if len(self.sma_200_queue) < (self.sma_200_period-1):
            self.sma_200_queue.append(close)
            self.test_plot.append_indicator_1(close)
            self.test_plot.append_indicator_2(close)
            # self.test_plot.append_indicator_3(close)

            if len(self.sma_5_queue) < (self.sma_5_period-1):
                self.sma_5_queue.append(close)
            else:
                self.current_5_sma = self.move_sma_5(close)

            if len(self.daily_gain_list) == 0:
                self.daily_gain_list.append(0)
                self.daily_loss_list.append(0)
                self.avg_gain_list.append(0)
                self.avg_gain_list.append(0)
            else:
                self.current_rsi = self.move_rsi(close)
            
            if len(self.daily_gain_list_2) == 0:
                self.daily_gain_list_2.append(0)
                self.daily_loss_list_2.append(0)
                self.avg_gain_list_2.append(0)
                self.avg_gain_list_2.append(0)
            else:
                self.current_rsi_2 = self.move_rsi_2(close)

            self.prev_close = close
            self.prev_volume = volume
            return "pass"
        try: 
            volume_percent_change = ((self.prev_volume - volume) / self.prev_volume) * 100
        except ZeroDivisionError:
            volume_percent_change = 0
        if volume_percent_change < 0:
            volume_percent_change = volume_percent_change * -1
        self.current_200_sma = self.move_sma_200(close)
        self.current_5_sma = self.move_sma_5(close)
        self.current_rsi = self.move_rsi(close)
        self.current_rsi_2 = self.move_rsi_2(close)
        self.test_plot.append_indicator_1(self.current_200_sma)
        self.test_plot.append_indicator_2(self.current_5_sma)
        # self.test_plot.append_indicator_3(self.current_rsi)
        # print(f"Current Close: {close}")
        # print(f"Current 200 SMA: {self.current_200_sma}")
        # print(f"Current 5 SMA: {self.current_5_sma}")
        # print(f"Current RSI: {self.current_rsi}")
        # print(f"Stradegy Started: {self.stradegy_started}")
        # print(f"Position: {self.position}")
        # print("\n")

        # time_short_1 = str(data["datetime"])
        # time_short_2 = time_short_1[0:10]
        # current_time = str(datetime.fromtimestamp(int(time_short_2)))
        # if current_time == "2022-07-14 10:00:00" or current_time == "2022-06-28 09:00:00":
        #     print(current_time)
        #     print(f"Current Close: {close}")
        #     print(f"Previous Close: {self.prev_close}")
        #     print(f"Current Volume: {volume}")
        #     print(f"Prev Volume: {self.prev_volume}")
        #     print(f"Current RSI 2: {self.current_rsi}")
        #     print(f"Current RSI 10: {self.current_rsi_2}")
        #     print("\n")

        # should probably put delay to let indicators get into zone
        # before running trade signals
        if self.counter <= 225:
            return "pass"
            
        # starting stradegy
        if self.stradegy_started == False:
            # if trend is bullish
            if self.current_200_sma < close:
                # if rsi in range 0-10
                if self.current_rsi < 5 and volume_percent_change > 40:
                    # open a short position
                    self.stradegy_started = True
                    self.position = False
                    # print(f"SELL TO OPEN\n")
                    return "sell"
                if self.current_rsi < 10 and (abs(self.current_rsi - self.current_rsi_2) > 60):
                    #  # open a short position
                    # self.stradegy_started = True
                    # self.position = False
                    # # print(f"SELL TO OPEN\n")
                    # return "sell"
                    return "pass"
                if self.current_rsi < 5: # and self.current_rsi >= 0:
                    # open long position
                    self.stradegy_started = True
                    self.position = True
                    # print(f"BUY TO OPEN\n")
                    return "buy"
            # elif trend is bearish
            elif self.current_200_sma > close:
                # if rsi is in range 90-100
                if self.current_rsi > 95 and volume_percent_change > 40:
                    # open a long position
                    self.stradegy_started = True
                    self.position = True
                    # print(f"BUY TO OPEN\n")
                    return "buy"
                if self.current_rsi > 90 and (abs(self.current_rsi - self.current_rsi) > 60):
                    # # open a long position
                    # self.stradegy_started = True
                    # self.position = True
                    # # print(f"BUY TO OPEN\n")
                    # return "buy"
                    return "pass"
                if self.current_rsi > 95: # and self.current_rsi <= 100:
                    # open a short position
                    self.stradegy_started = True
                    self.position = False
                    # print(f"SELL TO OPEN\n")
                    return "sell"

    
        # running stradegy 
        if self.stradegy_started == True:
            # if position is long
            if self.position == True:
                # close when prive moves above 5 sma
                if self.current_5_sma < close:
                    # close position
                    self.stradegy_started = False
                    self.position = None
                    # print(f"SELL TO CLOSE\n")
                    return "sell"
            # if position is short
            elif self.position == False:
                # close  when price moves below 5 sma
                if self.current_5_sma > close:
                    # close position
                    self.stradegy_started = False
                    self.position = None
                    # print(f"BUY TO CLOSE\n")
                    return "buy"


        # if none of the above validate return pass meaning
        # either holding or not entering position yet
        if self.stradegy_started == False:
            # print(f"NOT IN TRADE\n")
            pass
        else:
            # print(f"HOLDING\n")
            pass

        self.prev_close = close
        self.prev_volume = volume
        return "pass"


    def plot_stradegy(self):
        self.test_plot.plot()