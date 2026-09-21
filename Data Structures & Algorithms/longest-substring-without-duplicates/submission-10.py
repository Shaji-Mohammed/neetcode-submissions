class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        substr = set()

        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            
        return maxLen