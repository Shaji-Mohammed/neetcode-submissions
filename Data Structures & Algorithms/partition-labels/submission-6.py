class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
        res = []

        for i in s:
            counts[i] = 1 + counts.get(i, 0)
        
        counter = 0
        curr = ""
        for i in s:
            if i in counts:
                counts[i] -= 1
                counter += 1
                if i not in curr:
                    curr += i

            if counts[i] == 0:
                comp = True
                for c in curr:
                    if counts[c] != 0:
                        comp = False
                        break
                if comp:
                    res.append(counter)
                    counter = 0
                    curr = ""

        return res
