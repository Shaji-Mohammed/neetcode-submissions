class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        out = 0
        prev = intervals[0][1]

        for start, end in intervals[1:]:
            if prev > start:
                prev = min(end, prev)
                out += 1
            else:
                prev = end
        
        return out
