# pulls historical pricing data from polygon.io api
from polygon.authentication import config
import datetime
from datetime import timedelta
import requests


class Historical_Pricing:
    def __init__(self, ticker, period, start_date, end_date):
        self.ticker = ticker
        self.period = period
        self.start_date = start_date
        self.end_date = end_date
        self.csv_length = None

    def set_start_date_as_max(self):
        today_datetime = datetime.date.today()
        if self.period == 1:
            #period of every minute
            max_period = 17
            max_date = today_datetime - timedelta(days=max_period)
            self.start_date = (str(max_date))
        elif self.period == 2:
            #period of every 5 minutes
            max_period = 116 #9 months worth of trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.start_date = (str(max_date))
        elif self.period == 3:
            #period of every 10 minutes
            max_period = 118 #9 months worth of trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.start_date = (str(max_date))
        elif self.period == 4:
            #period of every 15 mintues
            max_period = 118 #9 months worth of trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.start_date = (str(max_date))
        elif self.period == 5:
            #period of every 30 minutes
            max_period = 119 #9 months worth of trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.start_date = (str(max_date))
        elif self.period == 6:
            #period of every day
            max_period = 6894 #back to 1985 in trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.start_date = (str(max_date))
        elif self.period == 7:
            #period of every week
            max_period = 10009 #back to 1985 in trading days
            max_date = today_datetime - timedelta(days=max_period)
            self.start_date = (str(max_date))
        else:
            #if user enters period of over 7 error is thrown
            raise IndexError("Period input not allowed.")

    def set_end_as_today(self):
        today_date = str(datetime.date.today())
        self.end_date = today_date

    def check_start_date(self):
        if self.start_date == None:
            #start date not provided
            self.set_start_date_as_max()

    def check_end_date(self):
        if self.end_date == None:
            #end date was not provided
            self.set_end_as_today()

    def get_multiplier(self):
        if self.period == 1:
            return 1
        elif self.period == 2:
            return 5
        elif self.period == 3:
            return 10
        elif self.period == 4:
            return 15
        elif self.period == 5:
            return 30
        elif self.period == 6:
            return 1
        elif self.period == 7:
            return 1
        else:
            return 1

    def get_timespan(self):
        if self.period == 1:
            return "minute"
        elif self.period == 2:
            return "minute"
        elif self.period == 3:
            return "minute"
        elif self.period == 4:
            return "minute"
        elif self.period == 5:
            return "minute"
        elif self.period == 6:
            return "day"
        elif self.period == 7:
            return "week"
        else:
            return "day"

    def get_csv_length(self):
        return self.csv_length
    
    def get_price_history(self):
        self.check_start_date()
        self.check_end_date()

        multiplier = self.get_multiplier()
        timespan = self.get_timespan()

        url = f"https://api.polygon.io/v2/aggs/ticker/{self.ticker}/range/{multiplier}/{timespan}/{self.start_date}/{self.end_date}?adjusted=true&sort=asc&limit=50000&apiKey={config.api_key}"

        http_response = requests.get(url)
        print(f"polygon feed: {http_response}")
        json_response = http_response.json()
        list_response = json_response['results']
        self.csv_length = len(list_response)

        for i in range(0, len(list_response)):
            dict_row = list_response[i]
            # dict_row.pop("vw")
            dict_row['open'] = dict_row.pop("o")
            dict_row['high'] = dict_row.pop("h")
            dict_row['low'] = dict_row.pop("l")
            dict_row['close'] = dict_row.pop("c")
            dict_row['volume'] = dict_row.pop("v")
            dict_row['datetime'] = dict_row.pop("t")
            # dict_row.pop('n')

        return list_response