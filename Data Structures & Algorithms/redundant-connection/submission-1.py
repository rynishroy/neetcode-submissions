class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(source, target, visited):
            if source == target:
                return True
            visited.add(source)
            for nei in adj[source]:
                if nei not in visited:
                    if dfs(nei, target,visited):
                        return True
            return False

        for u, v in edges:
            visited = set()
            if dfs(u,v, visited):
                return [u,v]

            adj[u].append(v)
            adj[v].append(u)




        