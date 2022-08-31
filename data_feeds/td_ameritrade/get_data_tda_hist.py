from td_ameritrade.authentication import oauth
import datetime
from datetime import timedelta
import pandas

# class based object that will contains a start date(current_date if not specified)
# in list form [day, month, year]
# end date(max days for period if not specified)
#  in list form [day, month, year], a frequency period of either:
# 1(every minute), 2(every 5 minutes), 3(every ten minutes), 4(every 15 minutes),
# 5(every 30 minutes), 6(every day), 7(every week)

class Historical_Pricing:
    def __init__(self, ticker, period):
        self.ticker = ticker
        self.start_date = None
        self.end_date = None
        self.period = period
        self.csv_length = None

    def set_start_date(self, start_date):
        #all dates should be passed in as year-month-day
        #and stored in class as list [day, month, year]
        start_date_list = []
        input_split = start_date.split("-") 
        start_date_list.append(input_split[2])
        start_date_list.append(input_split[1])
        start_date_list.append(input_split[0])
        self.start_date = start_date_list
        return self.start_date
    
    def set_end_date(self, end_date):
        #all dates should be passed in as year-month-day
        #and stored in class as list [day, month, year]
        end_date_list = []
        input_split = end_date.split("-")
        end_date_list.append(input_split[2])
        end_date_list.append(input_split[1])
        end_date_list.append(input_split[0])
        self.end_date = end_date_list
        return self.end_date
    
    def set_start_as_today(self):
        #if no start date is defined then current
        #date is used in format [day, month, year]
        today_date = str(datetime.date.today())
        today_date_list = today_date.split("-")
        start_day_list = []
        start_day_list.append(today_date_list[2])
        start_day_list.append(today_date_list[1])
        start_day_list.append(today_date_list[0])
        self.start_date = start_day_list
        return self.start_date
    
    def set_end_date_as_max(self):
        #if no end date is defined then max for
        #period is used in format [day, month, year]
        today_datetime = datetime.date.today()
        if self.period == 1:
            #every minute
            max_period = 17 #really 48 but we can ramp up later
            max_date = today_datetime - timedelta(days=max_period)
            self.set_end_date(str(max_date))
        elif self.period == 2:
            #every 5 minutes
            max_period = 116 #9 months worth of work days
            max_date = today_datetime - timedelta(days=max_period)
            self.set_end_date(str(max_date))
        elif self.period == 3:
            #every 10 minutes
            max_period = 118 #9 months worth of work days
            max_date = today_datetime - timedelta(days=max_period)
            self.set_end_date(str(max_date))
        elif self.period == 4:
            #every 15 mintues
            max_period = 118 #9 months worth of work days
            max_date = today_datetime - timedelta(days=max_period)
            self.set_end_date(str(max_date))
        elif self.period == 5:
            #every 30 minutes
            max_period = 119 #9 months worth of work days
            max_date = today_datetime - timedelta(days=max_period)
            self.set_end_date(str(max_date))
        elif self.period == 6:
            #every day
            max_period = 6894 #back to 1985
            max_date = today_datetime - timedelta(days=max_period)
            self.set_end_date(str(max_date))
        elif self.period == 7:
            # every week
            max_period = 10009 #back to 1985
            max_date = today_datetime - timedelta(days=max_period)
            self.set_end_date(str(max_date))
        else:
            raise IndexError("Period mode input not allowed.")
        return self.end_date

    def check_start_date(self):
        if self.start_date == None:
            start = self.set_start_as_today()
        else:
            return
            
    def check_end_date(self):
        if self.end_date == None:
            end = self.set_end_date_as_max()
        else:
            return

    def get_price_history(self):
        self.check_start_date()
        self.check_end_date()
        
        start_date_formatted = datetime.datetime(year = int(self.end_date[2]), month=int(self.end_date[1]), day=int(self.end_date[0]))
        end_date_formatted = datetime.datetime(year=int(self.start_date[2]), month=int(self.start_date[1]), day=int(self.start_date[0]))

        client = oauth.get_client()

        if self.period == 1:
            client_response = client.get_price_history_every_minute(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 2:
            client_response = client.get_price_history_every_five_minutes(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 3:
            client_response = client.get_price_history_every_ten_minutes(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 4:
            client_response = client.get_price_history_every_fifteen_minutes(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 5:
            client_response = client.get_price_history_every_thirty_minutes(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 6:
            client_response = client.get_price_history_every_day(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        elif self.period == 7:
            client_response = client.get_price_history_every_week(self.ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
        else:
            raise IndexError("Invalid period type to tda historical pricing -> must be 1 - 7 inclusivly.")

        df = pandas.read_json(client_response)
        csv_length = df.shape[0]
        df.to_csv(r'data_feeds\td_ameritrade\data_csvs\tda_historical.csv')
        return csv_length


# input syntax:
# - when initializing a Historical_Pricing object pass in the ticker, and period types
#   you have the option of setting the start and end dates but if not they will be set_end_date
#   to their max periods, the table for period types to pass in is as follows:
#     - 1, minute frequency period
#     - 2, five minute frequency period
#     - 3, ten mintue frequency period
#     - 4, fifteen minute freqiuency period
#     - 5, thirty minute frequency period
#     - 6, daily frequency period
#     - 7, weekly priving period

# sample input:
# i = 6
# data_test = Historical_Pricing("AAPL", i)
# csv_length = data_test.get_price_history()

# output:
# - the module outputs a csv containing the specified data for the period and 
#   ticker that was provided shelved in the 'data_csvs' folder
