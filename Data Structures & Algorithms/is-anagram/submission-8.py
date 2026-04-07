class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_list = [0] * 26
        t_list = [0] * 26
        matches = 0 

        for i in range(len(s)):
            s_list[ord(s[i]) - ord('a')] += 1
            t_list[ord(t[i]) - ord('a')] += 1

        for i in range(26):
            if s_list[i] == t_list[i]:
                matches += 1
            else:
                matches -= 1
            
        return matches == 26