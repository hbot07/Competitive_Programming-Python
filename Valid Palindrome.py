class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = -1

        while front - back != len(s) and (front < len(s)+back):

            if front >= len(s) or back < -len(s):
                break

            while not str.isalnum(s[front]):
                front += 1
                if front >= len(s) or back < -len(s):
                    break
            while not str.isalnum(s[back]):
                back -= 1
                if front >= len(s) or back < -len(s):
                    break

            if front >= len(s) or back < -len(s):
                break

            if s[front].lower() != s[back].lower():
                return False

            front += 1
            back -= 1

        return True


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
