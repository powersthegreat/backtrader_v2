#used for plotting and checking that stradegy looks right
import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime

class Plot_Stradegy:
    def __init__(self, show_plot, sim_name):
        self.show_plot = show_plot
        self.sim_name = sim_name
        self.close_list = []
        self.indicator_list_1 = []
        self.indicator_list_2 = []
        self.indicator_list_3 = []
        self.indicator_list_4 = []
        self.indicator_list_5 = []
    
    def append_close(self, close):
        self.close_list.append(close)
    
    def append_indicator_1(self, indicator_value):
        self.indicator_list_1.append(indicator_value)

    def append_indicator_2(self, indicator_value):
        self.indicator_list_2.append(indicator_value)

    def append_indicator_3(self, indicator_value):
        self.indicator_list_3.append(indicator_value)

    def append_indicator_4(self, indicator_value):
        self.indicator_list_4.append(indicator_value)

    def append_indicator_5(self, indicator_value):
        self.indicator_list_5.append(indicator_value)

    def plot(self):
        x_list = [i for i in range(len(self.close_list))]
        plt.figure()
        plt.plot(x_list, self.close_list, 'b')
        #plot stradegy as line
        # plt.plot(x_list, self.indicator_list, 'r')
        #plot stradegy as points
        for i in range(len(x_list)):
            if len(self.indicator_list_1) > 0:
                plt.scatter(x_list[i], self.indicator_list_1[i], color="r", s=8)
            if len(self.indicator_list_2) > 0:
                plt.scatter(x_list[i], self.indicator_list_2[i], color="b", s=8)
            if len(self.indicator_list_3) > 0:
                plt.scatter(x_list[i], self.indicator_list_3[i], color="r", s=8)
            if len(self.indicator_list_4) > 0:
                plt.scatter(x_list[i], self.indicator_list_4[i], color="b", s=8)
            if len(self.indicator_list_5) > 0:
                plt.scatter(x_list[i], self.indicator_list_5[i], color="r", s=8)


        plt.tight_layout()
        plt.savefig(f"stradegies\plotting\plots\stradegy_{self.sim_name}.png")
        print("plot stradegy: PASSED")
        if self.show_plot:
            plt.show()
