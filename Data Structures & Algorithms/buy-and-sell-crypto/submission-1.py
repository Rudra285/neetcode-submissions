class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         best = 0
         buy_price = float('inf')
         for i in range(len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                best = max(best, prices[i] - buy_price)
         return best