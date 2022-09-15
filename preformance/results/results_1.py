# results file:
# - getting orders from operate
# - creating:
#             - running P/L
#                           - send end to plot
#             - resulting record file:
#                                     - passed to plot class
from datetime import datetime
import csv

class Results:
    def __init__(self, ticker, source, order_size):
        self.ticker = ticker
        self.source = source
        self.order_size = order_size
        self.entry_price = 0
        self.p_and_l = 0
        self.p_and_l_list = []
        self.holding = False
        self.sim_records = []
        

    def running_p_and_l(self, data, order):
        #four cases
        if not self.holding and order == "buy":
            self.entry_price = float(data["close"])
            self.holding = True
            self.p_and_l_list.append(self.p_and_l)
            print("buy - holding")

        elif not self.holding and order == "sell":
            self.entry_price = float(data["close"])
            self.holding = True
            self.p_and_l_list.append(self.p_and_l)
            print("sell - holding")

        elif self.holding and order == "buy":
            self.p_and_l += (self.entry_price - float(data["close"]))*self.order_size
            self.p_and_l_list.append(self.p_and_l)
            print("buy - not holding")
            
        elif self.holding and order == "sell":
            self.p_and_l += (float(data["close"]) - self.entry_price)*self.order_size
            self.p_and_l_list.append(self.p_and_l)
            print("sell - not holding")

        else:
            self.p_and_l_list.append(self.p_and_l)
            pass
        

    def create_results(self, data, order):
        close_price = data["close"]
        #changes datetime stamp to normal ten digit stamp is in longer format
        if len(str(data["datetime"])) > 10:
            #if datetime longer than 10 digit version
            time_short_1 = str(data["datetime"])
            time_short_2 = time_short_1[0:10]
            time_stamp = str(datetime.fromtimestamp(int(time_short_2)))
        else:
            #datetime stamp is ten digit format
            time_stamp = str(datetime.fromtimestamp(data["datetime"]))

        if order != "pass":
            #adding to sim_records in list form [time_stamp, close_price, order]
            temp_order = []
            temp_order.append(time_stamp)
            temp_order.append(close_price)
            temp_order.append(order)
            temp_order.append(self.p_and_l)
            self.sim_records.append(temp_order)
            temp_order = []


    def write_results(self):
        feild_names = ["datetime", "close", "order", "P/L"]
        with open(f"preformance/results/csvs/simulation_records.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(feild_names)
            for i in range(0, len(self.sim_records)):
                writer.writerow(self.sim_records[i])
            csvfile.close()
        print("write results: PASSED")


    def pull_data_feed(self, data, order):
        self.running_p_and_l(data, order)
        self.create_results(data, order)


    def get_p_and_l_list(self):
        return self.p_and_l_list
    