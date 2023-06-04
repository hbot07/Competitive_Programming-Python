from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        open = []
        for i in height:
            if i > 0:
                open.append(i)
