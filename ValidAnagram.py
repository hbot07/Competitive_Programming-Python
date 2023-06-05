class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_dict1 = {}
        freq_dict2 = {}
        for i in s:
            if i not in freq_dict1:
                freq_dict1[i] = 0
                freq_dict2[i] = 0
            freq_dict1[i] += 1

        for i in t:
            if i not in freq_dict2:
                freq_dict2[i] = 0
                freq_dict1[i] = 0
            freq_dict2[i] += 1

        if len(freq_dict1) != len(freq_dict2):
            return False

        for i in freq_dict1:
            if freq_dict1[i] != freq_dict2[i]:
                return False
        for i in freq_dict2:
            if freq_dict1[i] != freq_dict2[i]:
                return False

        return True


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))
