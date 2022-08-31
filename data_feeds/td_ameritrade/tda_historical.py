from authentication import oauth
import datetime
from datetime import timedelta
import pandas

# class based object that will take in a start date(current_date if not specified)
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

    def get_every_minute(self):
        self.check_start_date()
        self.check_end_date()
        

for i in range(1, 8):
    data_test = Historical_Pricing("AAPL", i)
    data_test.get_every_minute()
    print("\n")

    

