class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf
        curMin, curMax = 1, 1


        for n in nums:
            temp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(temp, curMin * n, n)
            res = max(curMax, curMin, res)

        return res
