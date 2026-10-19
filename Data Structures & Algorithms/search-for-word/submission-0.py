class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW,COLS = len(board), len(board[0])
        res =[]
        visit=set()
        def dfs(r,c,pos):
            if pos ==len(word):
                return True
            if(r<0 or c<0 or r>=ROW or c>= COLS or board[r][c] != word[pos] or (r,c) in visit):
                return False
            visit.add((r,c))
            res = (dfs(r+1, c, pos+1) or
                   dfs(r-1, c, pos+1) or
                   dfs(r, c+1, pos+1) or
                   dfs(r, c-1, pos+1))
            visit.remove((r,c))
            return res

        for r in range(ROW):
            for c in range(COLS):
                if dfs(r,c,0): return True
        return False
        