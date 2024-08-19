class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # this is essentially just a standard binary search
        # the challenge is that we can't merge the arrays due to TC restraints
        # need to use some form of manipulating the index we're searching to treat the arrays
        # as if they were just one long array 
        lenRow, lenCol = len(matrix[0]), len(matrix)
        l, r = 0, (lenRow * lenCol) - 1

        while l <= r:
            m = (l + r)//2
            row, col = (m // lenRow),(m % lenRow)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1
        return False


        
                               


