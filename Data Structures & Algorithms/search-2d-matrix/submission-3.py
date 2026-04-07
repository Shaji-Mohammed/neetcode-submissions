class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0]) - 1

        row = -1

        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][len(matrix[0])-1]:
                row = i

        while l < r:
            mid =  (r + l) // 2
            temp = matrix[row][mid]
            if temp == target:
                return True
            elif temp > target:
                r = mid - 1
            else:
                l = mid + 1

        if matrix[row][l] == target:
            return True
        return False


