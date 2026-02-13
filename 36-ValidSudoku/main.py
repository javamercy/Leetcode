from collections import defaultdict


class Solution1:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for x, cells in enumerate(board):
            for y, cell in enumerate(cells):
                if cell == ".":
                    continue
                if (not self.isValidRow(board, x, y, cell)
                        or not self.isValidCol(board, x, y, cell)
                        or not self.isValidBox(board, x, y, cell)):
                    return False
        return True

    def isValidRow(self, board: list[list[str]], x: int, y: int, cell: str):
        for i in range(9):
            if i == y:
                continue
            if board[x][i] == cell:
                return False
        return True

    def isValidCol(self, board: list[list[str]], x: int, y: int, cell: str):
        for i in range(9):
            if i == x:
                continue
            if board[i][y] == cell:
                return False
        return True

    def isValidBox(self, board: list[list[str]], x: int, y: int, cell: str):
        row_start = (x // 3) * 3
        col_start = (y // 3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if i == x and j == y:
                    continue
                if board[i][j] == cell:
                    return False
        return True


class Solution2:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for x, cells in enumerate(board):
            for y, cell in enumerate(cells):
                if cell == ".":
                    continue

                box = (x // 3) + (y // 3) * 3
                if (cell in rows[x]
                        or cell in cols[y]
                        or cell in boxes[box]):
                    return False

                rows[x].add(cell)
                cols[y].add(cell)
                boxes[box].add(cell)

        return True
