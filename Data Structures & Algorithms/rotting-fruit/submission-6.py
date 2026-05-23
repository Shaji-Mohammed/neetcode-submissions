class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    count += 1

        def rottenT(r, c):
            if (0 > r or r == rows or 0 > c or c == cols or grid[r][c] != 1):
                return 
            grid[r][c] = 2
            q.append([r, c])
            nonlocal count 
            count -= 1
            
        time = 0
        while q and count > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                

                rottenT(r + 1, c)
                rottenT(r, c + 1)
                rottenT(r - 1, c)
                rottenT(r, c - 1)
            time += 1

        return -1 if count else time


