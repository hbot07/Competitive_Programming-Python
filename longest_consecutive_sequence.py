from typing import List


class int_obj:
    def __init__(self, value):
        self.value = value

    def add(self, opearand):
        self.value += opearand

    def __cmp__(self, other):
        return self.value - other.value

    def __gt__(self, other):
        return self.value - other.value > 0


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        consecutive_dict = {}
        for i in nums:
            if i not in consecutive_dict:
                consecutive_dict[i] = int_obj(1)
                if (i - 1 in consecutive_dict) and (i + 1 in consecutive_dict):
                    sum = consecutive_dict[i - 1].value + consecutive_dict[i + 1].value + 1
                    consecutive_dict[i - 1].value = sum
                    consecutive_dict[i + 1].value = sum
                    consecutive_dict[i] = consecutive_dict[i - 1]
                    consecutive_dict[i + 1] = consecutive_dict[i - 1]
                else:
                    if i - 1 in consecutive_dict:
                        consecutive_dict[i - 1].value = consecutive_dict[i - 1].value + 1
                        consecutive_dict[i] = consecutive_dict[i - 1]
                    if i + 1 in consecutive_dict:
                        consecutive_dict[i + 1].value = consecutive_dict[i + 1].value + 1
                        consecutive_dict[i] = consecutive_dict[i + 1]
        print([(key, value.value) for key, value in consecutive_dict.items()])
        nums.sort()
        print(nums)
        return max(consecutive_dict.values()).value


nums = [-6,-9,8,-8,-1,-3,-6,8,-9,-1,-4,-8,-5,0,1,6,-8,-5,-7,8,-2,-8,4,5,-5,-1,-5]
print(Solution().longestConsecutive(nums))
