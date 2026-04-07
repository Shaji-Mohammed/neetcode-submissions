class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nd = {}
        for i in range(len(nums)):
            nd[nums[i]] = i

        for i in range(len(nums)):
            r = target - nums[i]
            ind = nd.get(r)
            if ind and i != ind:
                return [i, ind]