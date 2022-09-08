#class acts as driver of all specific data pulling classes in the folders below
#it (e.g. td_ameritrade). takes in all member variables when called in the operate
#class. in charge of creating csv from data source, converting the csv into a
#pandas data frame, and sending increments of this dataframe in order to the operate
#class when called upon

import sys
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\data_feeds\td_ameritrade')
import get_data_tda_hist as tda_hist
import csv
import pandas   


class Feed_Historical_Pricing:
    def __init__(self, ticker, source, period, start_date, end_date):
        #class takes a ticker(as string value), a period (integer 1-7 inclusive
        #representing the frequency between data), a start date (string in form
        #"year-month-day"), and a end date (string in form "year-month-date").
        #also holds variables for csv length which it gets from the respected
        #data feed source, and a object to store the csv converted date frame
        #(historical_pricing_df)

        self.ticker = ticker
        self.source = source
        self.period = period
        self.source = source
        self.start_date = start_date
        self.end_date = end_date
        self.csv_length = None
        self.historical_pricing_df = None


    def create_csv(self):
        #method creates csv by calling method from the class associated with the source
        #memeber variable, from this class the length of the created csv is returned as well
    
        if self.source == "tda":
            #creating csv from td ameritrade data feed
            data_test = tda_hist.Historical_Pricing(self.ticker, self.period, self.start_date, self.end_date)
            csv_length = data_test.get_price_history()
            self.csv_length = csv_length    
        elif self.source == "yahoo":
            #creating csv from yahoo finance data feed
            pass
        else:
            #throwing error if source passed in is not one of options, these options should keep
            #expanding though as more official and credible data feed api's are added
            raise InterruptedError("Invalid source, please choose from: 'tda', 'yahoo', or 'bloomberg'.")  

    def read_csv(self):
        #method reads from the created csv given the source member variable, all csvs are stored in
        #a ordered location in the location as follows '<source>/<source>_csv/<source>_historical.csv'
        #from their given location they are read using pandas and created into a dataframe which is
        #stored in the historical_pricing_df memeber variable

        if self.source == "tda":
            #reading from tda csv and converting to dataframe
            self.historical_pricing_df = pandas.read_csv("data_feeds/td_ameritrade/data_csvs/tda_historical.csv")
        elif self.source == "yahoo":
            #reading from yahoo finance csv and converting to dataframe
            pass
        else:
            #throwing error as second check for invalid source type
            raise InterruptedError("Invalid source, please choose from: 'tda', 'yahoo', or 'bloomberg'.")

    def get_increment_df(self, index):
        #method pulls a single line from the historical_pricing_df, converts it into
        #a cleaned dictionary in the form as follows ;
        #{'open': <int open>, 'high': <int high>, 'low': <int low>, 'close': <int close>, 'volume': <int volume>, 'datetime': <int datetime stamp>}
        #this dictionary is returned to operate to be used in other classes

        if self.source == "tda":
            #eval function takes dictionary converted to string back to dictionary
            #(stored as string from tda, !specific to tda!)
            current_row_dict = eval(self.historical_pricing_df.loc[index][1])
            #returning/pushing data increment to operate class
            return current_row_dict
        elif self.source == "yahoo":
            pass
        else:
            #throwing error as third check for invalid source type
            raise InterruptedError("Invalid source, please choose from: 'tda', 'yahoo', or 'bloomberg'.")

    def get_length(self):
        #returns length of csv
        return self.csv_length
    

