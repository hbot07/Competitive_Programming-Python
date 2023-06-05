from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1]
        for i in nums:
            p.append(p[-1] * i)

        s = [1]
        nums_reverse = nums.copy()
        nums_reverse.reverse()
        for i in nums_reverse:
            s.append(s[-1] * i)

        answer = []

        for i in range(len(nums)):
            answer.append(p[i] * s[len(nums) - i - 1])
        # print(p, s, answer)
        return answer


nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
