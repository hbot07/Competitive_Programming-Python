from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2

            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1

        k = l


        i = lambda a: (a+k)%len(nums)
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2

            if nums[i(mid)] == target:
                return i(mid)
            else:
                if nums[i(mid)] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


nums = [4,5,6,7,0,1,2]
target = 3
print(Solution().search(nums, target))

