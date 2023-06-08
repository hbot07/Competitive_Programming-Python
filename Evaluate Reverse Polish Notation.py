from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 0:
            return 0
        for i in tokens:
            if str.isdigit(i[-1]):
                stack.append(i)
                # print("digit added ", stack, i)
            else:
                b = stack.pop()
                a = stack.pop()
                result = eval(a + i + b)
                stack.append(str(int(result)))
                print(a+i+b, result)
                # print("eval done ", stack)
            # print("end ", stack)
        return int(float(stack.pop()))


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))
