from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Edge case: empty matrix
        if not matrix or not matrix[0]:
            return 0

        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prevValue):
            if (r < 0 or r == ROWS or c < 0 or c == COLS) or matrix[r][c] <= prevValue:
                # If we are out of bounds, we return 0.
                # If we are in bounds but matrix[r][c] <= prevValue, this path is invalid, return 0.
                return 0
                
            if (r, c) in dp:
                return dp[(r, c)]
            
            # Explore all 4 neighbors
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            
            dp[(r, c)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
                
        return max(dp.values())
