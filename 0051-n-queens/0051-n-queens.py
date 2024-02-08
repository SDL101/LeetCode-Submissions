class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        resBoards = []
        currBoard = [["." for _ in range(n)] for _ in range(n)]
        col = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in currBoard]
                resBoards.append(copy)
                return
            # loop through each col in the current row
            for c in range(n):
                # if current cell is already in any of 3 sets
                # skip to next  iteration of the loop (check next column)
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                else:
                    col.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                    currBoard[r][c] = "Q"
                
                    backtrack(r+1)

                    col.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)
                    currBoard[r][c] = "."
                
        #start at row 0
        backtrack(0)
        return resBoards