class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = count = 0
        for num in nums:
            count +=1 if num else -count
            res = max(res, count)
        return res