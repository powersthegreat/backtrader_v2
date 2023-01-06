import sys

sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\data_feeds\td_ameritrade\authentication')
import oauth

import datetime
import pandas

client = oauth.get_client()

# formatting for startdate and enddate, very  hard to get so don't lose it!
start_date = datetime.datetime(year=2022, month=3, day=4)
end_date = datetime.datetime(year=2022, month=3, day=14)
# print(start_date)
# print(end_date)
ticker = "AAPL"
response = client.get_price_history_every_thirty_minutes(ticker, start_datetime=start_date, end_datetime=end_date, need_extended_hours_data=None)
# print(json.dumps(response.json(), indent=4))
print(response)
#creating a csv from historical price json
# df = pandas.read_json(response)
# df.to_csv (r'test_tda.csv'+ticker, index = None)
