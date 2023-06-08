class MinStack:

    def __init__(self):
        self.stack = []
        self.minima = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minima) == 0:
            self.minima.append(val)
        else:
            if self.minima[-1] >= val:
                self.minima.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minima[-1]:
            self.minima.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minima[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
