class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = {}
        tMap = {}

        for i in range(len(s)):
            si = s[i]
            sMap[si] = 1 + sMap.get(si, 0)
            ti = t[i]
            tMap[ti] = 1 + tMap.get(ti, 0)            
        
        return True if sMap == tMap else False