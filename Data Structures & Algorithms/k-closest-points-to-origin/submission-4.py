class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i,j in points:
            temp = (i** 2) + (j** 2)
            minHeap.append([temp, i, j])

        heapq.heapify(minHeap)
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res    
            
        
