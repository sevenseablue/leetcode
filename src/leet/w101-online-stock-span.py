class StockSpanner:

    def __init__(self):

        self.prices = []
        self.greater = []
        pass

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.prices.append(price)
        ind = len(self.greater)-1
        while ind>=0 and price >= self.prices[ind]:
            ind = self.greater[ind]
        self.greater.append(ind)

        return len(self.prices) - ind - 1



# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
for price in [100, 80, 60, 70, 60, 75, 85]:
    param_1 = obj.next(price)
    print(param_1)