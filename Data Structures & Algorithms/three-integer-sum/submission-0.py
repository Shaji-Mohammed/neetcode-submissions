class Solution:

    def pair_sum_sorted(self, nums: List[int], target: int):
        left, right = 0, len(nums) -1
        arr = set()
        while(left < right):
            sum = nums[left] + nums[right]
            if (sum > target):
                right = right - 1 
            elif (sum < target):
                left = left + 1
            else:
                triplet = [-target, nums[left], nums[right]]
                arr.add(tuple(triplet))
                right = right - 1 
                left = left + 1

        return arr
            

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i,j,k = 0,1,2

        arr = set()
        length = len(nums)
        nums.sort()

        for i in range(length):
            pairs = self.pair_sum_sorted(nums[i+1: length], -nums[i])

            if pairs: 
                for triplet in pairs:
                    arr.add(triplet)

        return list(arr)

