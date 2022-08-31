
# operate doesn't seem like it needs to be class based...but may
# be useful in the future so I will make it this way

class Operate_Historical():
    def __init__(self):
        self.length_csv = None

    def pull_data(self):
        pass
    #     get start row of historical csv
    #     get end row of historical csv (probably 0 or while True):
    #         iterate through from start row to end
    #         this will be the incrementation of the operate file
    #         it will call a get_increment method from a data feed
    #         class and and recieve a dicitonary line of the 'current'
    #         data then be able to use this data with stradegy modules