# Runtime 105 ms Beats 72.62%
# Memory 16.4 MB Beats 27.93%

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_valid_row(row):
                return False

        for col in zip(*board):
            if not self.is_valid_row(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid_row(grid):
                    return False

        return True

    def is_valid_row(self, row):
        numbers = set()
        for num in row:
            if num != '.':
                if num in numbers:
                    return False
                numbers.add(num)
        return True
