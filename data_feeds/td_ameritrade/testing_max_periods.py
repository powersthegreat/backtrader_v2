from authentication import oauth
import datetime
import pandas
from datetime import timedelta
import json

# client = oauth.get_client()

# todays_date_list = str(datetime.date.today()).split("-")
# end_date_formatted = datetime.datetime(year=int(todays_date_list[0]), month=int(todays_date_list[1]), day=int(todays_date_list[2]))
# differences = [100, 1000, 5000, 10000, 20000, 50000, 75000]

# for day_difference in differences:
#     start_date = str(datetime.date.today() - timedelta(days = day_difference)).split("-")
#     start_date_formatted = datetime.datetime(year=int(start_date[0]), month=int(start_date[1]), day=int(start_date[2]))
    
#     ticker = "AAPL"
#     # response = client.get_price_history_every_minute(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
#     # response = client.get_price_history_every_five_minutes(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
#     # response = client.get_price_history_every_ten_minutes(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
#     # response = client.get_price_history_every_fifteen_minutes(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
#     # response = client.get_price_history_every_thirty_minutes(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
#     # response = client.get_price_history_every_day(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
#     response = client.get_price_history_every_week(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
#     print(response)
#     df = pandas.read_json(response)
#     df.to_csv (r'test_tda'+str(day_difference)+r'.csv', index = None)


client = oauth.get_client()

todays_date_list = str(datetime.date.today()).split("-")
end_date_formatted = datetime.datetime(year=int(todays_date_list[0]), month=int(todays_date_list[1]), day=int(todays_date_list[2]))

day_difference = 10000

start_date = str(datetime.date.today() - timedelta(days = day_difference)).split("-")
start_date_formatted = datetime.datetime(year=int(start_date[0]), month=int(start_date[1]), day=int(start_date[2]))

ticker = "AAPL"

responses = []

response_1 = client.get_price_history_every_minute(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
responses.append(response_1)
response_2 = client.get_price_history_every_five_minutes(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
responses.append(response_2)
response_3 = client.get_price_history_every_ten_minutes(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
responses.append(response_3)
response_4 = client.get_price_history_every_fifteen_minutes(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
responses.append(response_4)
response_5 = client.get_price_history_every_thirty_minutes(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
responses.append(response_5)
response_6 = client.get_price_history_every_day(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
responses.append(response_6)
response_7 = client.get_price_history_every_week(ticker, start_datetime=start_date_formatted, end_datetime=end_date_formatted, need_extended_hours_data=True)
responses.append(response_7)

response_types = ["minute", "five_minute", "ten_minute", "fifteen_minute", "thirty_minute", "day", "week"]
counter = 0

for i in range(0, len(responses)):
    df = pandas.read_json(responses[i])
    df.to_csv (r'test_tda_'+response_types[i]+'.csv', index = None)
   