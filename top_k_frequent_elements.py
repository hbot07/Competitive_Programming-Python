from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 0
            freq_dict[i] += 1

        lr = [(-value, key) for key, value in freq_dict.items()]

        import heapq

        heapq.heapify(lr)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(lr))

        return [key for value, key in ans]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
