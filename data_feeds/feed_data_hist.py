from td_ameritrade import get_data_tda_hist as tda_hist
import csv
from pandas
class Feed_Historical_Pricing:
    def __init__(self):
        self.csv_start = None
        self.csv_end = None
        self.csv_length = None
        self.df = None
    
    def read_csv_tda(self, period):
        
        
    def create_tda_csv(self, period):
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

    def get_length(self):
        return self.csv_length

    def get_increment_tda(self, index):
        #pulls a single line of the csv at the index given
        #converts it into a dictionary
        #and returns the dicitonary (to be called by and 
        #fed to operate class)
        pass

    
        