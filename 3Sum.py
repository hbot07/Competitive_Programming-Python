import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int, left) -> List[List[int]]:
        right = len(numbers) - 1
        answer = []
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                answer.append([left, right])
                left += 1
            else:
                if total < target:
                    left += 1
                else:
                    right -= 1
        return answer

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums [i-1]:
                two_sum_result = self.twoSum(nums, -nums[i], i + 1)
                # print(two_sum_result)
                if len(two_sum_result) == 0:
                    continue
                else:
                    for j in two_sum_result:
                        answer.append([nums[i], nums[j[0]], nums[j[1]]])
        ans = []
        for i in answer:
            i.sort()
            if i not in ans:
                ans.append(i)

        return ans


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
