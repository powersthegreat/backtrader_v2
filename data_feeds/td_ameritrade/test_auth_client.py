from authentication import oauth
import datetime
import pandas

client = oauth.get_client()

# formatting for startdate and enddate, very  hard to get so don't lose it!
start_date = datetime.datetime(year=2022, month=3, day=4)
end_date = datetime.datetime(year=2022, month=3, day=14)

response = client.get_price_history_every_thirty_minutes('SND', start_datetime=start_date, end_datetime=end_date, need_extended_hours_data=None)
# print(json.dumps(response.json(), indent=4))

#creating a csv from historical price json
df = pandas.read_json (response)
df.to_csv (r'test_tda.csv', index = None)
