# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
from typing import List


class Solution:
    perms = []

    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in {'(', '[', '{'}:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if i != parentheses[popped]:
                    return False

        return len(stack) == 0

    def gen(self, n, perm):
        if n == 0:
            if self.isValid(perm):
                self.perms.append(perm)
            return
        else:
            self.gen(n - 1, perm + ')')
            self.gen(n - 1, perm + '(')

    def generateParenthesis(self, n: int) -> List[str]:
        self.gen(n * 2, "")
        return self.perms


n = 1
print(Solution().generateParenthesis(n))
