from typing import List


class Solution:
    def convert(self, index, r):
        return index // r, index % r

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix[0])
        col_len = len(matrix)
        l = 0
        r = row_len * col_len - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[self.convert(mid, row_len)[0]][self.convert(mid, row_len)[1]] == target:
                return True
            else:
                if matrix[self.convert(mid, row_len)[0]][self.convert(mid, row_len)[1]] > target:
                    r = mid - 1
                else:
                    l = mid + 1

        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(Solution().searchMatrix(matrix, target))
