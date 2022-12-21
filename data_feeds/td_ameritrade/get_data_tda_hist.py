#pulls historical pricing from td ameritrades developer api using
#the tda-api built by alex golec

import sys
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\data_feeds\td_ameritrade\authentication')
import oauth
import datetime
from datetime import timedelta
import pandas

class Historical_Pricing:
    def __init__(self, ticker, period, start_date, end_date):
        #class takes a ticker(as string value), a period (integer 1-7 inclusive
        #representing the frequency between data), a start date (string in form
        #"year-month-day"), and a end date (string in form "year-month-date").

        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.period = period

    def set_start_date(self, start_date):
        #method to set start date, pass in choosen start date in string of 
        #form "year-month-day" and member variable is returned in list form 
        #[day, month, year]

        start_date_list = []
        input_split = start_date.split("-") 
        start_date_list.append(input_split[2])
        start_date_list.append(input_split[1])
        start_date_list.append(input_split[0])
        self.start_date = start_date_list
        return self.start_date
    
    def set_end_date(self, end_date):
        #method to set end date, pass in choosen start date in string of 
        #form "year-month-day" and member variable is returned in list form 
        #[day, month, year]

        end_date_list = []
        input_split = end_date.split("-")
        end_date_list.append(input_split[2])
        end_date_list.append(input_split[1])
        end_date_list.append(input_split[0])
        self.end_date = end_date_list
        return self.end_date
    
    def set_end_as_today(self):
        #if no end date is defined then current
        #date is used in list form [day, month, year]

        today_date = str(datetime.date.today())
        today_date_list = today_date.split("-")
        end_day_list = []
        end_day_list.append(today_date_list[2])
        end_day_list.append(today_date_list[1])
        end_day_list.append(today_date_list[0])
        self.end_date = end_day_list
        return self.end_date
    
    def set_start_date_as_max(self):
        #if no start date is provided function pushes start date
        #to 'max' possible length for period and returns it in list
        #form [day, month, year]

        '''
        need to test and find maximum end dates using plotted results
        '''

        today_datetime = datetime.date.today()
        if self.period == 1:
            #period of every minute
            max_period = 17 #really 48 but we can ramp up later
            max_date = today_datetime - timedelta(days=max_period)
            self.set_start_date(str(max_date))
        elif self.period == 2:
            #period of every 5 minutes
            max_period = 116 #9 months worth of trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.set_start_date(str(max_date))
        elif self.period == 3:
            #period of every 10 minutes
            max_period = 118 #9 months worth of trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.set_start_date(str(max_date))
        elif self.period == 4:
            #period of every 15 mintues
            max_period = 118 #9 months worth of trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.set_start_date(str(max_date))
        elif self.period == 5:
            #period of every 30 minutes
            max_period = 119 #9 months worth of trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.set_start_date(str(max_date))
        elif self.period == 6:
            #period of every day
            max_period = 6894 #back to 1985 in trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.set_start_date(str(max_date))
        elif self.period == 7:
            #period of every week
            max_period = 10009 #back to 1985 in trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.set_start_date(str(max_date))
        else:
            #if user enters period of over 7 error is thrown
            raise IndexError("Period input not allowed.")
        return self.start_date

    def check_start_date(self):
        #method sets the start date as either the current date, if no
        #start date was provided, or calls set_start_date which formats
        #the inputted start date into list form [day, month, year]

        if self.start_date == None:
            #start date not provided
            start = self.set_start_date_as_max()
        else:
            #start date provided
            self.set_start_date(self.start_date)
            
    def check_end_date(self):
        #method sets end date as either max date for period, if no end date
        #was provided, or calls set_end_date which formats the inputted
        # end date into list form [day, month, year]

        if self.end_date == None:
            #end date was not provided
            end = self.set_end_as_today()
        else:
            #end date was provided
            self.set_end_date(self.end_date)

    def get_price_history(self):
        #main driver method of get_data_tda_hist module, first checks dates, then
        #formats them too date time objects, then intializes a client object from
        #the oauth module, then calls the corresponding data fetching method form
        #tda-api depending on the inputted period, finally converts the response to 
        #a csv containing incremental data relating to the inputted ticker and dates

        #checking and setting start date
        self.check_start_date()
        #checking and setting end date
        self.check_end_date()
        
        #formatting start date too datetime object
        start_date_formatted = datetime.datetime(year = int(self.start_date[2]), month=int(self.start_date[1]), day=int(self.start_date[0]))
        #formatting end date to datetime object
        end_date_formatted = datetime.datetime(year=int(self.end_date[2]), month=int(self.end_date[1]), day=int(self.end_date[0]))

        #initializing client object from oauth module
        client = oauth.get_client()

        if self.period == 1:
            #increment of 1 minute across date range
            client_response = client.get_price_history_every_minute(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 2:
            #increment of 5 minutes across date range
            client_response = client.get_price_history_every_five_minutes(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 3:
            #increment of 10 minutes across date range
            client_response = client.get_price_history_every_ten_minutes(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 4:
            #increment of 15 minutes across date range
            client_response = client.get_price_history_every_fifteen_minutes(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 5:
            #increment of 30 minutes across date range
            client_response = client.get_price_history_every_thirty_minutes(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 6:
            #increment of 1 day across date range
            client_response = client.get_price_history_every_day(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 7:
            #increment of 1 week across date range
            client_response = client.get_price_history_every_week(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        else:
            #back up period check if any of set date error throws don't catch
            raise IndexError("Invalid period type to tda historical pricing -> must be 1 - 7 inclusivly.")
        #using pandas to read http json response
        print(f"tda feed: {client_response}")
        df = pandas.read_json(client_response)
        #df.shape returns a tuple of the length and width of the data frame, the [0]
        #index sets csv_length to the length of the dataframe
        csv_length = df.shape[0]
        #csv is built in form "row#, increment data, ticker, after_hours_data(T/F)"
        df.to_csv(r'data_feeds\td_ameritrade\data_csvs\tda_historical.csv')
        #the length of the csv(found from dataframe) is returned to be used in later processes
        return csv_length


