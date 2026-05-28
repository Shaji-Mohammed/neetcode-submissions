class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {e:[] for e in range(n)}

        for s, e in edges:
            edgeMap[s].append(e)
            edgeMap[e].append(s)

        visiting = set()

        def dfs(node, prev):
            if node in visiting:
                return False
            
            visiting.add(node)

            for e in edgeMap[node]:
                if prev == e:
                    continue
                if not dfs(e, node):
                    return False
            
            return True
        

        return dfs(0, -1) and len(visiting) == n