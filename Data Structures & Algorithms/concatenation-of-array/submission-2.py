class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        dup = []
        for i in nums:
            dup.append(i)

        for i in nums:
            dup.append(i)

        return dup