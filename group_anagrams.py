from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dicts = [{} for _ in strs]
        for j in range(len(strs)):
            for i in strs[j]:
                if i not in freq_dicts[j]:
                    freq_dicts[j][i] = 0
                freq_dicts[j][i] += 1

        taken = [False for _ in strs]
        grouped = []
        for i in range(len(strs)):
            ana = []
            if not taken[i]:
                ana.append(strs[i])
                taken[i] = True

            for j in range(i + 1, len(strs)):
                if not taken[j]:
                    if freq_dicts[i] == freq_dicts[j]:
                        ana.append(strs[j])
                        taken[j] = True

            if len(ana) > 0:
                grouped.append(ana)
        return grouped


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
