from typing import List


class Solution:
    def rob(self, cost: List[int]) -> int:
        a = cost[0]
        b = cost[1]
        c = 0
        if len(cost) <= 2:
            return min(a, b)
        cost.append(0)
        cost.append(0)
        for i in range(len(cost)):
            if i > 1:
                c = min(a, b) + cost[i]
                a = b
                b = c

        return max(c)