class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0, 0
        freq = {}
        longest = max_len = 0

        while r < len(s):
            freq.update({s[r]: freq.get(s[r], 0) + 1})
            longest = max(longest, freq[s[r]])

            if (r - l + 1) - longest > k:
                freq[s[l]] -= 1
                l += 1
            max_len = r - l + 1
            r +=1

        return max_len