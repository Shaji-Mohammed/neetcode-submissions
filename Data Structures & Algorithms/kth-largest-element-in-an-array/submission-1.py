class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-num for num in nums]
        heapq.heapify(minHeap)

        result = 0

        for i in range(k):
            result = -heapq.heappop(minHeap)

        return result