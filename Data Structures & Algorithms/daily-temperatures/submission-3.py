class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i, v in enumerate(temperatures):
            if i == 0:
                stk.append(i)
                continue
            while stk and v > temperatures[stk[len(stk)- 1]]:
                res[stk[len(stk)-1]] = (i - stk[len(stk)-1])
                stk.pop()
            stk.append(i)

        return res