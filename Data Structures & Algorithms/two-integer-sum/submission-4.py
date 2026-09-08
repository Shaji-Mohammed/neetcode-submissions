class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i,v in enumerate(nums):
            rem = (target - v)
            if rem in track:
                return [track.get(rem), i]
            else:
                track[v] = i
