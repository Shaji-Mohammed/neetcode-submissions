class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(n1):
            if n1 != par[n1]:
                par[n1] = find(par[n1])
            return par[n1]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            else:
                par[p1] = par[p2]
                rank[p2] += rank[p1]

            return True

        for u,v in edges:
            if not union(u, v):
                return [u,v]