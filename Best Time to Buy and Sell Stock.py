from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.reverse()
        maxima = prices[0]
        max_profit = 0
        for i in prices:
            if maxima < i:
                maxima = i
            if max_profit < maxima - i:
                max_profit = maxima - i
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
