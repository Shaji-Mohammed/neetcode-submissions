# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
#         k = 0
#         large = 0

#         for i in piles:
#             large = max(large, i)

#         ks = [p for p in range(1, large)]

#         l, r = 0, large - 1

#         while l < r:
#             mid = (l+r)//2
#             hours = 0
#             for i in piles:
#                 hours = hours + math.ceil(i/mid)

#             if hours < h:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#             k = hours
        
#         return k

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res