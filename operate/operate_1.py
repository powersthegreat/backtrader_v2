import sys
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\data_feeds')
import feed_data_hist
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\preformance')
import preformance_1

# C:\Users\Owner\Desktop\backtrader_v2\data_feeds\feed_data_hist.py
# C:\Users\Owner\Desktop\backtrader_v2\operate\operate_1.py
# operate doesn't seem like it needs to be class based...but may
# be useful in the future so I will make it this way

class Operate_Historical():
    def __init__(self, ticker, source, period=6, show_plot=True, start_date=None, end_date=None):
        self.ticker = ticker
        self.source = source
        self.period = period
        self.show_plot = show_plot
        self.start_date = start_date
        self.end_date = end_date
        self.csv_length = None
        self.loaded_data_obj = None

    def load_data(self):
        loaded_data = feed_data_hist.Feed_Historical_Pricing(self.ticker, self.source, self.period, self.start_date, self.end_date)
        loaded_data.create_csv()
        loaded_data.read_csv()
        self.csv_length = loaded_data.csv_length
        self.loaded_data_obj = loaded_data
        print("load data: PASSED")

    def run_simulation(self):
        #start object of graph and records class
        preformance = preformance_1.Preformance(self.source, self.ticker, self.show_plot)
        #start object of stradegy class
        for i in range(0, self.csv_length): #should be self.csv_length
            row_dict = self.loaded_data_obj.get_increment_df(i)
            #send row dict to graph class
            preformance.push_to_order_dict_and_records(row_dict, "pass")
            #send row dict to stradegy class
            #if stradegy returns "nothing" -> continue
            #elif stradegy returns "buy" ->
            # - mark it on the graph
            # - send appropriate data to record object
            #elif stradegy returns "sell" ->
            # - mark it on the graph
            # - send appropriate data to records object
        preformance.generate_results()
        print("run simulation: PASSED")




# input syntax:
# - when initializing a Operate_Historical object pass in the ticker, data feed source,
#   period type, an optional start and end date in form "YEAR-MONTH-DAY", and a optional
#   'True' or 'False' if you want the plot to show on the screen. You have the option of 
#   setting the start and end dates but if not they will be set to their max periods, the
#   table for period types to pass in is as follows:
#     - 1, minute frequency period
#     - 2, five minute frequency period
#     - 3, ten mintue frequency period
#     - 4, fifteen minute freqiuency period
#     - 5, thirty minute frequency period
#     - 6, daily frequency period
#     - 7, weekly priving period

test_1 = Operate_Historical(ticker="bruh", source="tda", period=6, start_date="2022-8-1", end_date="2022-9-1", show_plot=True)
# test_1 = Operate_Historical(ticker="TSLA", source="tda", period=6)
test_1.load_data()
test_1.run_simulation()
