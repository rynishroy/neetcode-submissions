class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if m + n != len(s3):
            return False
        
        # m+1 rows, n+1 columns
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        
        # FIXED: Loop r over rows (m+1) and c over columns (n+1)
        for r in range(m + 1):
            for c in range(n + 1):
                if c > 0 and dp[r][c-1] and s1[c-1] == s3[c-1+r]:
                    dp[r][c] = True
                if r > 0 and dp[r-1][c] and s2[r-1] == s3[r-1+c]:
                    dp[r][c] = True
                    
        return dp[-1][-1]




        