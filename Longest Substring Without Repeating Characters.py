class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        streak = 0
        max_streak = 0
        i = 0
        while i < len(s):
            if s[i] not in chars:
                chars.add(s[i])
                streak += 1
                if streak > max_streak:
                    max_streak = streak
                i += 1
            else:
                chars.remove(s[i - streak])
                streak -= 1
        return max_streak


s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
