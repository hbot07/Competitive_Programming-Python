class Solution:
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


s = "()"
s = "(]"
print(Solution().isValid(s))
