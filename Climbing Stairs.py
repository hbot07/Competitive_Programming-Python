class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        c = 3
        if n <= 3:
            return n

        for i in range(n):
            if i > 1:
                c = a + b
                a = b
                b = c

        return c
