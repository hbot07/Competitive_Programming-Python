class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq_dict = {}
        for i in range(len(s)):
            if s[i] in