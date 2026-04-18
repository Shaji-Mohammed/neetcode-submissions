class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
        res = []

        for i, v in enumerate(s):
            counts[v] = max(i, counts.get(v, 0))
        
        counter = 0
        lastIndex = 0
        for i, v in enumerate(s):
            lastIndex = max(counts[v], lastIndex)
            counter+=1

            if i == lastIndex:
                res.append(counter)
                counter = 0

        return res
