from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = [[1 for j in range(i + 1)] for i in range(numRows)]

        def get(p, r, c):
            if c < 0 or c >= len(p[r]):
                return 0
            else:
                return p[r][c]

        for i in range(numRows):
            for j in range(i + 1):
                pascals_triangle[i][j] = get(pascals_triangle, i - 1, j - 1) + get(pascals_triangle, i - 1, j)

        return pascals_triangle


print(Solution().generate(5))
