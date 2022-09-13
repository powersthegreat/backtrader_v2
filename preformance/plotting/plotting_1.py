# plot results:
# - data feed passed in from operate
# - order passed in from operate
# - saves and shows matplotlib plot
# - needs to get P/L from results class

import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime


class Plot:
    def __init__(self, source, ticker, show_plot):
        self.source = source
        self.ticker = ticker
        self.show_plot = show_plot
        self.order_dict = {}
        self.sim_records = []
        self.p_and_l_list = None

    def pull_data_feed(self, data, order):
        #takes in a data increment (in dictionary form), and a order
        #either "pass", "buy", or "sell". then pushes this data into
        #the order_dict, sim_records is only pushed too if order is
        #not "pass" (still recorded to order_dict)
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

        #adding price details to order_dict in form key(timestamp) -> value([close, order])
        self.order_dict[time_stamp] = [close_price, order]
        if order != "pass":
            #adding to sim_records in list form [time_stamp, close_price, order]
            temp_order = []
            temp_order.append(time_stamp)
            temp_order.append(close_price)
            temp_order.append(order)
            self.sim_records.append(temp_order)
            temp_order = []


    def plot_results(self):
        #method plots results of stradegies preformance by use of order_dict and sim_records
        #member variables

        '''
        work in progress as would like to see cleaner and more official looking
        '''

        #creating datetimes list to be x axis
        times_list = list(self.order_dict.keys())
        order_list = list(self.order_dict.values())
        #creating close lsit to be y axis
        close_list = [i[0] for i in order_list]
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(times_list, close_list, 'r')
        plt.title(f"{self.source} feed for {self.ticker}")
        plt.xlabel("close")
        plt.ylabel("timestamp")

        for sim_order in self.sim_records:
            if sim_order[2] == "buy":
                plt.scatter(sim_order[0], sim_order[1]-2, color='g', s=25, marker="^")
            elif sim_order[2] == "sell":
                plt.scatter(sim_order[0], sim_order[1]+2, color='r', s=25, marker="v")
            else:
                raise RuntimeError("Order was not 'buy' or 'sell'.")
        
        plt.subplot(2, 1, 2)
        plt.plot(times_list, self.p_and_l_list, 'b')
        plt.xlabel("P/L")
        plt.ylabel("timestamp")

        plt.tight_layout()
        plt.savefig("preformance\plotting\plots\sim_plot.png") #dpi=1000 as parameter?
        print("plot results: PASSED")
        if self.show_plot == True:
            plt.show()
    
    def push_p_and_l_list(self, p_and_l_list):
        self.p_and_l_list = p_and_l_list

    