class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowChecker = defaultdict(set)
        colChecker = defaultdict(set)
        boxChecker = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowChecker[r] or board[r][c] in colChecker[c] or board[r][c] in boxChecker[(r//3, c//3)]):
                    return False
                rowChecker[r].add(board[r][c])
                colChecker[c].add(board[r][c])
                boxChecker[(r//3, c//3)].add(board[r][c])
        return True
                