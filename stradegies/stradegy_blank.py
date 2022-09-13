class Stradegy:
    def __init__(self, order_size):
        self.order_size = order_size
        self.current_order = None
        self.period = 10
        self.period_queue = []

    def logic(self, data):
        order = "pass"
        return order