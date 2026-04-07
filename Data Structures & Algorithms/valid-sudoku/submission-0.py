class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        grid_sets = [[set() for _ in range(3)]for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                if num in rows[i]:
                    return False
                if num  in col_sets[j]:
                    return False                    
                if num in grid_sets[i // 3][j // 3]:
                    return False                    

                rows[i].add(num)
                col_sets[j].add(num)
                grid_sets[i // 3][j // 3].add(num)
        return True
