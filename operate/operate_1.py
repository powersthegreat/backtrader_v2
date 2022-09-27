#the main driver of the software, in charge of pulling data from feed classes
#sending data too preformance classes (graphing and records), and sending
#data to the stradegy class then receiving signals and executing

'''
work still in progress, need some sort of P/L tracking class,
buy/sell order 'routes', and probably more
'''

import sys
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\data_feeds')
import feed_data_hist
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\preformance\plotting')
import plotting_1
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\stradegies')
import stradegy_2
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\preformance\results')
import results_1


class Operate_Historical():
    def __init__(self, ticker, source, period=6, show_plot=False, start_date=None, end_date=None, order_size=100):
        #class takes a ticker(as string value), a source(as a string value), a 
        #period (integer 1-7 inclusive representing the frequency between data), 
        #a start date (string in form "year-month-day"), and a end date (string 
        #in form "year-month-date"). also holds a show plot variable(if user wants
        #plot to pop up on the screen), and a loaded data object used for storing
        #data feed object

        self.ticker = ticker
        self.source = source
        self.period = period
        self.show_plot = show_plot
        self.start_date = start_date
        self.end_date = end_date
        self.csv_length = None
        self.loaded_data_obj = None
        self.order_size = order_size

    def load_data(self):
        #method calls Feed_Historical_Pricing method from feed_data_hist
        #module passing in the ticker, source, period, and start+end dates
        #creates the csv, reads the csv, stores the created csv length
        #and stores the data feed object created to be used in the 
        #run_simulation method

        loaded_data = feed_data_hist.Feed_Historical_Pricing(self.ticker, self.source, self.period, self.start_date, self.end_date)
        loaded_data.create_csv()
        loaded_data.read_csv()
        #saving csv length to memeber variable
        self.csv_length = loaded_data.csv_length
        self.loaded_data_obj = loaded_data
        print("load data: PASSED")

    def run_simulation(self):
        #start object of stradegy class
        stradegy = stradegy_2.Stradegy(self.order_size)
        #start object of graph class
        plot = plotting_1.Plot(self.source, self.ticker, self.show_plot)
        #start object of results class
        result = results_1.Results(self.ticker, self.source, self.order_size)

        for i in range(0, self.csv_length): #should be self.csv_length
            row_dict = self.loaded_data_obj.get_increment_df(i)
            #send row dict to stradegy class
            order = stradegy.logic(row_dict)
            #send row dict to graph class
            plot.pull_data_feed(row_dict, order)
            #send row dict to results class
            result.pull_data_feed(row_dict, order)
            
        #pulling profit and loss list from results class
        p_and_l_list = result.get_p_and_l_list()
        #pushing profit and loss list to plotting class
        plot.push_p_and_l_list(p_and_l_list)
        #plotting close vrs time and P/L vrs time
        plot.plot_results()
        #plotting stradegy vrs time and close vrs time
        stradegy.plot_stradegy()
        #writing order results to csv file form results class
        result.write_results()
        #signaling simulation is over
        print("run simulation: PASSED")




# initialization input syntax:
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

test_1 = Operate_Historical(ticker="AAPL", source="tda", period=5, start_date="2022-8-1", end_date=None, show_plot=True, order_size=100)
test_1.load_data()
test_1.run_simulation()