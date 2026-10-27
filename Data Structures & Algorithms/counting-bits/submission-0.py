class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize DP array of size n + 1 with 0s
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # dp[i >> 1] gets the bit count of i divided by 2
            # (i & 1) adds 1 if the current number is odd
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp