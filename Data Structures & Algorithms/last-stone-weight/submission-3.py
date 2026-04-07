class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            highest = -heapq.heappop(maxHeap)
            high = -heapq.heappop(maxHeap)
            temp = highest - high

            # if temp > 0: 
            heapq.heappush(maxHeap, -temp)
            
        return -maxHeap[0]
        