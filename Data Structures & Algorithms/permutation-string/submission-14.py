class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for i in s1:
            need[i] = need.get(i, 0) + 1

        l = 0

        for r in range(len(s2)):


            window[s2[r]] = window.get(s2[r], 0) + 1

            if (r - l + 1) > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    window.pop(s2[l])
                l += 1
            
            if need == window:
                return True
            
        return False