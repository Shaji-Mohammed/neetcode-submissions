class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l+r) // 2
            hours = 0

            for i in piles:
                hours += math.ceil(i / mid)

            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
                res = min(mid, res)
            
        
        return res

        