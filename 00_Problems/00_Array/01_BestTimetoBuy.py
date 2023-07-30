class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0

        for value in prices:
            min_price = min(min_price, value)
            tmp_price = value - min_price
            max_profit = max(max_profit, tmp_price)

        return max_profit
