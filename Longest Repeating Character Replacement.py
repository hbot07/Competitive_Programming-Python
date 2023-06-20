class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set()
        i = 0
        streak = 0
        max_streak = 0
        while i < len(s):
            if len(chars) == 1:
                if s[i] in chars:
                    streak += 1
                else:
                    if k > 0:
                        k -= 1
                        streak += 1
                    else:
                        streak = 0
                        chars = set()
                max_streak = max(max_streak, streak)

            if len(chars) == 0:
                chars.add(s[i])
                streak = 1
            i += 1

        return max_streak


s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))
