"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        count = 0
        max_count = 0
        sp = 0
        ep = 0

        while sp < len(start):
            if start[sp] < end[ep]:
                count += 1
                sp += 1
            else:
                ep += 1
                count -= 1 

            max_count = max(max_count, count)

        return max_count