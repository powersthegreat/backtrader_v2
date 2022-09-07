#for testing purposes only

import matplotlib
from matplotlib import pyplot as plt
import pandas
import csv
from datetime import datetime

historical_pricing_df = pandas.read_csv("data_feeds/td_ameritrade/data_csvs/tda_historical.csv")
close_list = []
times_list = []

for i in range(0, len(historical_pricing_df)):
    current_dict = eval(historical_pricing_df.loc[i][1])
    close_list.append(current_dict["close"])
    time_short_1 = str(current_dict["datetime"])
    time_short_2 = time_short_1[0:10]
    time_stamp = str(datetime.fromtimestamp(int(time_short_2)))
    times_list.append(time_stamp)


times_list_2000 = '2011-09-30 00:00:00'
times_list_3000 = '2015-09-23 00:00:00'
times_list_4000 = '2019-09-13 00:00:00'

plt.figure()
plt.rcParams.update({'font.size':5})
plt.plot(times_list, close_list, 'k')
plt.scatter(times_list_2000, 50, color='g', s=25, marker="^")
plt.scatter(times_list_3000, 100, color='r', s=25, marker="v")
plt.scatter(times_list_4000, 150, color='g', s=25, marker="^")

plt.xlabel("Date")
plt.ylabel("Price")
plt.savefig("test_plot.png", dpi=1000)
plt.show()

