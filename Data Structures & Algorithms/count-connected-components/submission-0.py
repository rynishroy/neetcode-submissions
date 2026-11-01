class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i:[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        numComponents = 0

        def dfs(i):
            visited.add(i)
            for nei in adj[i]:
                if nei not in visited:
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                numComponents +=1
        return numComponents




        