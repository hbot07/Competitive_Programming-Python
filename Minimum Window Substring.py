class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = {}
        for i in t:
            if i in dict_t:
                dict_t[i] += 1
            else:
                dict_t[i] = 1

        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), 0, 0
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


s = "ABAC"
t = "ABC"
print(Solution().minWindow(s, t))
