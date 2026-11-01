class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[float("inf")] * (len(word2)+1) for _ in range(len(word1)+1)]

       # Base case: converting empty word1 to word2[j:] requires insertions
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j

        # Base case: converting word1[i:] to empty word2 requires deletions
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i
        
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1+ min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        return dp[0][0]

        