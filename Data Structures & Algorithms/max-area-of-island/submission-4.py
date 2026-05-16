class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        maxLen = curLen = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, curLen):
            grid[r][c] = -1
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for dr, dc in directions:
                nr, nc = dr + r, c + dc
                if  0 <= nr and nr < rows and 0 <= nc and nc < cols and grid[nr][nc] == 1:
                    curLen += 1
                    curLen = dfs(nr, nc, curLen)

            return curLen

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxLen = max(maxLen, dfs(r, c, curLen + 1))
                    curLen = 0
        
        return maxLen
