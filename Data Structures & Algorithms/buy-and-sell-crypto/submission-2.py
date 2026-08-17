class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        profit = 0
        for i in prices:
            lowest = min(lowest, i)
            profit = max(i - lowest, profit)
        return profit
