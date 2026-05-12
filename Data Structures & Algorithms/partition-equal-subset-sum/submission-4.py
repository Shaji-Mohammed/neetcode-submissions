class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for n in range(len(nums)-1, -1, -1):
            nextDP = set()
            for t in dp:
                if t == target:
                    return True
                nextDP.add(t + nums[n])
                nextDP.add(t)
            dp = nextDP
        
        return True if target in dp else False

