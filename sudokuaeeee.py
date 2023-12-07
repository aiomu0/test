from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Checking for strings
        for row in board:
            if not self.is_valid_unit(row):
                return False

        # Checking for columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_valid_unit(column):
                return False

        # Checking for sub board 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid_unit(square):
                    return False

        return True

    def is_valid_unit(self, unit: List[str]) -> bool:
        seen = set()
        for cell in unit:
            if cell != ".":
                if cell in seen:
                    return False
                seen.add(cell)
        return True


if __name__ == "__main__":
    sudoku_solver = Solution()

    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    print('Input:')
    for i in range(9):
        print(board1[i])
    print('Output: ', sudoku_solver.isValidSudoku(board1))

    print('Input:')
    for i in range(9):
        print(board2[i])
    print('Output: ', sudoku_solver.isValidSudoku(board2))
