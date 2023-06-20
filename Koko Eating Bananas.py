import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            mid = (l+r)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
            print("try", mid, hours)
            if hours <= h:
                r = mid
            else:
                l = mid + 1
        return r


piles = [30,11,23,4,20]
h = 6
print(Solution().minEatingSpeed(piles, h))