import sys
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\data_feeds')
import feed_data_hist
sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\preformance')
import preformance_1

# C:\Users\Owner\Desktop\backtrader_v2\data_feeds\feed_data_hist.py
# C:\Users\Owner\Desktop\backtrader_v2\operate\operate_1.py
# operate doesn't seem like it needs to be class based...but may
# be useful in the future so I will make it this way

class Operate_Historical():
    def __init__(self, source):
        self.csv_length = None
        self.source = source
        self.loaded_data_obj = None

    def load_data(self):
        loaded_data = feed_data_hist.Feed_Historical_Pricing(self.source)
        loaded_data.create_csv()
        loaded_data.read_csv()
        self.csv_length = loaded_data.csv_length
        self.loaded_data_obj = loaded_data

    def run_simulation(self):
        #start object of graph and records class
        preformance = preformance_1.Preformance()
        #start object of stradegy class
        for i in range(0, self.csv_length): #should be self.csv_length
            row_dict = self.loaded_data_obj.get_increment_df(i)
            #send row dict to graph class
            preformance.push_to_order_dict_and_records(row_dict, "pass")
            #send row dict to stradegy class
            #if stradegy returns "nothing" -> continue
            #elif stradegy returns "buy" ->
            # - mark it on the graph
            # - send appropriate data to record object
            #elif stradegy returns "sell" ->
            # - mark it on the graph
            # - send appropriate data to records object
        preformance.generate_results()

            

test_1 = Operate_Historical("tda")
test_1.load_data()
test_1.run_simulation()
