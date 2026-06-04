class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowChecker = defaultdict(set) #hashmap (key: row index, value: set of all nums in that row to verify existence)
        colChecker = defaultdict(set) #hashmap (key: col index, value: set of all nums in that col to verify existence)
        boxChecker = defaultdict(set) #hashmap (key: master row and col index pair (considering each 3x3 box to be its own index, found through integer division by 3 since we know number of boxes), value: set of all values in that box to verify existence)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowChecker[r] or board[r][c] in colChecker[c] or board[r][c] in boxChecker[(r//3, c//3)]): #no need to convert to tuple, just do the r//3 and c//3 computation in the subscript
                    return False
                rowChecker[r].add(board[r][c]) #add is the operation to add to a set
                colChecker[c].add(board[r][c])
                boxChecker[(r//3, c//3)].add(board[r][c])
        return True
                