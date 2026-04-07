class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        longest, length = 0, 0
        tracker = set()

        while r < len(s):
            if s[r] not in tracker:
                tracker.add(s[r])
                length +=1
                r += 1
                longest = max(length, longest)
            else:
                tracker.remove(s[l])
                l += 1
                length -= 1
        return longest
