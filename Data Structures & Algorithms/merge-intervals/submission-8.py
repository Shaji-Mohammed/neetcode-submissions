class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        out = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = out[-1][1]

            if start <= lastEnd:
                out[-1][1] = max(end, lastEnd)
            else:
                out.append([start, end])

        return out