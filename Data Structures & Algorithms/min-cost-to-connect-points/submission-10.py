class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        V = len(points)
        totalCost = 0
        adj = {i:[] for i in range(V)} #[cost, node]

        for i in range(V):
            x1, y1 = points[i]
            for j in range(i + 1, V):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                
                adj[i].append([cost, j])
                adj[j].append([cost, i])


        # prim's
        minHeap = [[0, 0]]
        visited = set()

        while len(visited) < V:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            totalCost += cost
            visited.add(node)

            for neiCost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])

        return totalCost
