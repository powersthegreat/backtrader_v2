import sys
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\data_feeds\td_ameritrade')
import get_data_tda_hist as tda_hist
import csv
import pandas   


class Feed_Historical_Pricing:
    def __init__(self, source):
        self.csv_length = None
        self.historical_pricing_df = None
        self.source = source
        

    def create_csv(self, period = 6):
        if self.source == "tda":
            # input syntax:
            #     - 1, minute frequency period
            #     - 2, five minute frequency period
            #     - 3, ten mintue frequency period
            #     - 4, fifteen minute freqiuency period
            #     - 5, thirty minute frequency period
            #     - 6, daily frequency period
            #     - 7, weekly priving period
            # more on 'get_tda_hist' module
            data_test = tda_hist.Historical_Pricing("AAPL", period)
            csv_length = data_test.get_price_history()
            self.csv_length = csv_length    
        elif self.source == "yahoo":
            pass
        else:
            raise InterruptedError("Invalid source, please choose from: 'tda', 'yahoo', or 'bloomberg'.")  

    def read_csv(self):
        #pass in either tda, yahoo, bloomberg, or somthing else down the line
        if self.source == "tda":
            self.historical_pricing_df = pandas.read_csv("data_feeds/td_ameritrade/data_csvs/tda_historical.csv")
        elif self.source == "yahoo":
            pass
        else:
            raise InterruptedError("Invalid source, please choose from: 'tda', 'yahoo', or 'bloomberg'.")

    def get_increment_df(self, index):
        #pulls a single line of the df memeber variable,
        #converts that line to a dictionary of form 
        #{'open': 160.305, 'high': 160.58, 'low': 157.14, 'close': 157.22, 'volume': 68435470, 'datetime': 1661918400000}
        #and returns it for use of operate
        if self.source == "tda":
            current_row_dict = eval(self.historical_pricing_df.loc[index][1])
            return current_row_dict
        elif self.source == "yahoo":
            pass
        else:
            raise InterruptedError("Invalid source, please choose from: 'tda', 'yahoo', or 'bloomberg'.")

    def get_length(self):
        return self.csv_length
    

# test_1 = Feed_Historical_Pricing("tda")
# test_1.create_csv(6)
# test_1.read_csv()
# test_1.get_increment_df(0)
# df_length = test_1.get_length()
# test_1.get_increment_df(df_length-1)