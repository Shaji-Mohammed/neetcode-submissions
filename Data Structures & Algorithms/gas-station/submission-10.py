class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        index = 0
        g = 0
        for i in range(len(gas)):
            g += (gas[i] - cost[i])
            if g < 0:
                g = 0
                index = i + 1

        
        return index