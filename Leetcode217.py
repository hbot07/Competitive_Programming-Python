from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_dict = {}
        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 0
            freq_dict[i] += 1

        for i in freq_dict:
            if freq_dict[i] > 1:
                return True
        return False


nums = [1, 2, 3, 4]
print(Solution().containsDuplicate(nums))
