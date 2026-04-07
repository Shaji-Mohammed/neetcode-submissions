class Solution:
    def isValid(self, s: str) -> bool:
        _dict = {
            '(':')',
            '[': ']',
            '{':'}',
        }
        l = len(s)
        _stack = []

        for i in s:
            if i in _dict.keys():
                _stack.append(i)
            elif _stack and _dict[_stack.pop()] == i:
                continue
            else:
                return False
        
    
        return not _stack