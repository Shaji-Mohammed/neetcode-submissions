class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def check_pal(l, r, resLen):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    res = s[l:r + 1]

                l -= 1
                r += 1

        for i in range(len(s)):
            # odd len
            l, r = i, i
            # check_pal(l, r, resLen)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    res = s[l:r + 1]

                l -= 1
                r += 1

            l, r = i, i+1
            # check_pal(l, r, resLen)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    res = s[l:r + 1]

                l -= 1
                r += 1
        
        return res

            
