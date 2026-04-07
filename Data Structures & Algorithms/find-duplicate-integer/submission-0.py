class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        record = set()

        for i in nums:
            if i in record:
                return i
            else:
                record.add(i)
        