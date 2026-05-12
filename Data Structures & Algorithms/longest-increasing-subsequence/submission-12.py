class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for n in range(len(nums)-1, -1, -1):
            for j in range(n+1, len(nums)):       
                if nums[j] > nums[n]:
                    dp[n] = max(1 + dp[j], dp[n])
        

        return max(dp)