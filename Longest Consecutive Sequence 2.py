from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxima = 0
        streak = 0
        for num in nums:
            streak = 0
            if num-1 not in num_set:
                while num in num_set:
                    num += 1
                    streak += 1
                maxima = max(maxima, streak)
        return maxima

