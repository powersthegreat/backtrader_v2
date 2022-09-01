from ..data_feeds.feed_data_hist import Feed_Historical_Pricing

# operate doesn't seem like it needs to be class based...but may
# be useful in the future so I will make it this way

class Operate_Historical():
    def __init__(self, source):
        self.csv_length = None
        self.source = None

    def load_data(self):
        feed_data_hist.create_csv()
        feed_data_hist.read_csv()
        self.csv_length = feed_data_hist.csv_length
        print(self.csv_length)


test_1 = Operate_Historical("tda")
test_1.load_data()


    