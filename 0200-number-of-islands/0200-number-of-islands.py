class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque([(r,c)])

            while q:
                row, col = q.popleft()
                directions = [(1,0), (-1,0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc

                    if (0 <= newRow < rows and 
                        0 <= newCol < cols and
                        grid[newRow][newCol] == '1' and  
                        (newRow, newCol) not in visited): 

                        q.append((newRow, newCol))
                        visited.add((newRow, newCol))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands