class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create a default dict with the key as a tuple (r, c) and the value as a set of the numbers in the (r, c)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        #iterate over each cell on the board
        for r in range(len(board)):
            for c in range(len(board[0])):
                #check if it's in the set for 1. row, 2. col, 3. box
                #return false if it already exists in any of those 3 sets
                cell = board[r][c]
                if cell == ".":
                    continue
                if (cell in rows[r] or cell in cols[c] or cell in boxes[(r//3, c//3)]):
                    print(rows, cols, boxes)
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[(r//3, c//3)].add(cell)
        return True    