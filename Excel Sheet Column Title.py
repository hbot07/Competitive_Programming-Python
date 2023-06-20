class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = []
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            s.append(chr(columnNumber % 26 + 65))
            columnNumber = columnNumber // 26

        s.reverse()
        return "".join(s)


print(Solution().convertToTitle(1))
