class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float('inf')
        profit = 0
        for price in prices:
            lowest_price = min(lowest_price, price)
            profit = max(price - lowest_price, profit)
        return profit
