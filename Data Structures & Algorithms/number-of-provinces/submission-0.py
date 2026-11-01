class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        self.visited = set()
        province = 0

        def dfs(i):
            self.visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and j not in self.visited:
                    dfs(j)
            return
        for i in range(n):
            if i not  in self.visited:
                province +=1
                dfs(i)

        return province
        