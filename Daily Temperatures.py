from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in temperatures]
        for i in range(len(temperatures) - 1, -1, -1):
            j = i + 1
            while j<len(temperatures):
                if temperatures[i] < temperatures[j]:
                    answer[i] = j - i
                    break
                if answer[j] == 0:
                    break
                j += answer[j]
        return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
