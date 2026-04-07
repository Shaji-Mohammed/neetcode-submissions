class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = (len(nums) - 1)
        lowest = nums[0]

        while l <= r:

            if nums[l] < nums[r]:
                lowest = min(nums[l], lowest)
                break

            mid = (r + l) // 2
            lowest = min(nums[mid], lowest)

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        
        
        return lowest

            
