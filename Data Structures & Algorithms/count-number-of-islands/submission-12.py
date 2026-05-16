class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            grid[r][c] = -1
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr) and (nr < rows) and (0 <= nc) and (nc < cols) and (grid[nr][nc] == "1"):
                    dfs(nr, nc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands