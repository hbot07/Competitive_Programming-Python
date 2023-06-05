from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [i for i in board]
        columns = [[i[j] for i in board] for j in range(9)]
        boxes = []
        for i in range(3):
            for j in range(3):
                # print(3 * i, 3 * j)
                boxes.append(board[3 * i][3 * j:3 * j + 3] + board[3 * i + 1][3 * j:3 * j + 3] +
                             board[3 * i + 2][3 * j:3 * j + 3])
        # print(rows, columns, boxes, sep="\n")
        for i in rows + columns + boxes:
            freq_dict = {}
            for j in i:
                if j != ".":
                    if j not in freq_dict:
                        freq_dict[j] = 0
                    freq_dict[j] += 1
            for key, value in freq_dict.items():
                if value > 1:
                    return False
        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(Solution().isValidSudoku(board))
