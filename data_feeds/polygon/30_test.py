
import sys
sys.path.append(r"C:\Users\Owner\Desktop\backtrader_v2\data_feeds\polygon")
import get_data_polygon_hist as polygon_hist
import pandas

ticker = "SPY"
period = 5
start_dates = ["2022-04-01", "2022-06-02", "2022-08-02", "2022-10-02"]
end_dates = ["2022-06-01", "2022-08-01", "2022-10-01", "2022-12-01"]

historical_pricing_df = None
for i in range(len(start_dates)):
    data_test = polygon_hist.Historical_Pricing(ticker, period, start_dates[i], end_dates[i])
    if historical_pricing_df == None:
        historical_pricing_df = data_test.get_price_history()
    else:
        historical_pricing_df += data_test.get_price_history()

df = pandas.DataFrame.from_dict(historical_pricing_df)
df.to_csv("30_test.csv")

