from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0
        while l < r:
            mid = (l + r) // 2

            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]


nums = [2,3,4,5,1]
print(Solution().findMin(nums))
