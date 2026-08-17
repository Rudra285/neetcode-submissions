class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] >= min_price:
                curr_profit = prices[i] - min_price
                profit = max(profit, curr_profit)
        return profit
