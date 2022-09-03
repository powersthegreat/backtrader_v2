import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime
import csv

class Preformance:
    def __init__(self):
        self.order_dict = {}
        self.sim_records = []
        
    def push_to_order_dict_and_records(self, data, order):
        close_price = data["close"]
        if len(str(data["datetime"])) > 10:
            time_short_1 = str(data["datetime"])
            time_short_2 = time_short_1[0:10]
            time_stamp = str(datetime.fromtimestamp(int(time_short_2)))
        else:
            time_stamp = str(datetime.fromtimestamp(data["datetime"]))

        self.order_dict[time_stamp] = [close_price, order]
        if order != "pass":
            temp_order = []
            temp_order.append(time_stamp)
            temp_order.append(close_price)
            temp_order.append(order)
            self.sim_records.append(temp_order)
            temp_order = []
    

    def plot_results(self):
        times_list = list(self.order_dict.keys())
        order_list = list(self.order_dict.values())
        close_list = [i[0] for i in order_list]
        plt.figure()
        plt.plot(times_list, close_list)
        plt.savefig("preformance\plots\sim_plot.png")
        print("Plotted")
    
    def write_sim_records(self):
        feild_names = ["datetime", "close", "order"]
        with open("preformance\sim_records\sim_records.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(feild_names)
            for i in range(0, len(self.sim_records)):
                writer.writerow(self.sim_records[i])
            csvfile.close()
        
    def generate_results(self):
        self.write_sim_records()
        self.plot_results()



# test_dict_data = [
#     {'open': 166.37, 'high': 167.81, 'low': 164.2, 'close': 164.87, 'volume': 60362338, 'datetime': 1659934800000},
#     {'open': 164.02, 'high': 165.82, 'low': 163.25, 'close': 164.92, 'volume': 63135503, 'datetime': 1660021200000},
#     {'open': 167.68, 'high': 169.34, 'low': 166.9, 'close': 169.24, 'volume': 70170540, 'datetime': 1660107600000},
#     {'open': 170.06, 'high': 170.99, 'low': 168.19, 'close': 168.49, 'volume': 57149159, 'datetime': 1660194000000},
#     {'open': 169.82, 'high': 172.17, 'low': 169.4, 'close': 172.1, 'volume': 68039382, 'datetime': 1660280400000},
#     {'open': 171.52, 'high': 173.39, 'low': 171.345, 'close': 173.19, 'volume': 54091694, 'datetime': 1660539600000},
#     {'open': 172.78, 'high': 173.71, 'low': 171.6618, 'close': 173.03, 'volume': 56377050, 'datetime': 1660626000000},
#     {'open': 172.77, 'high': 176.15, 'low': 172.57, 'close': 174.55, 'volume': 79542037, 'datetime': 1660712400000},
#     {'open': 173.75, 'high': 174.9, 'low': 173.12, 'close': 174.15, 'volume': 62290075, 'datetime': 1660798800000},
#     {'open': 173.03, 'high': 173.74, 'low': 171.3101, 'close': 171.52, 'volume': 70346295, 'datetime': 1660885200000},
#     {'open': 169.69, 'high': 169.86, 'low': 167.135, 'close': 167.57, 'volume': 69026809, 'datetime': 1661144400000},
#     {'open': 167.08, 'high': 168.71, 'low': 166.65, 'close': 167.23, 'volume': 54147079, 'datetime': 1661230800000},
#     {'open': 167.32, 'high': 168.11, 'low': 166.245, 'close': 167.53, 'volume': 53841524, 'datetime': 1661317200000},
#     {'open': 168.78, 'high': 170.14, 'low': 168.35, 'close': 170.03, 'volume': 51218209, 'datetime': 1661403600000},
#     {'open': 170.57, 'high': 171.05, 'low': 163.56, 'close': 163.62, 'volume': 78960980, 'datetime': 1661490000000},
#     {'open': 161.145, 'high': 162.9, 'low': 159.82, 'close': 161.38, 'volume': 73313953, 'datetime': 1661749200000},
#     {'open': 162.13, 'high': 162.56, 'low': 157.72, 'close': 158.91, 'volume': 77906197, 'datetime': 1661835600000},
#     {'open': 160.305, 'high': 160.58, 'low': 157.14, 'close': 157.22, 'volume': 87991091, 'datetime': 1661922000000},
#     {'open': 156.64, 'high': 158.42, 'low': 154.67, 'close': 157.96, 'volume': 74229896, 'datetime': 1662008400000},
#     {'open': 159.75, 'high': 160.362, 'low': 154.965, 'close': 155.82, 'volume': 65691117, 'datetime': 1662091200000}
#     ]

# order_test = ["pass", "pass", "pass", "buy", "sell","pass", "pass", "pass", "buy", "sell","pass", "pass", "pass", "buy", "sell","pass", "pass", "pass", "buy", "pass"]

# test_1 = Preformance()
# for i in range(0, len(test_dict_data)):
#     test_1.push_to_order_dict_and_records(test_dict_data[i], order_test[i])

# test_1.write_sim_records()
# test_1.graph_results()
