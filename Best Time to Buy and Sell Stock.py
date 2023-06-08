from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxima = prices[0]
        minima = prices[0]
        profit = 0
        for i in prices:
            if maxima < i:
                maxima = i
            if minima > i:
                minima = i
            if profit < maxima - minima:
                profit = maxima - minima
        return profit


prices = [7, 1, 5, 3, 6, 4]
print()
