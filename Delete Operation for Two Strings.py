# 583. Delete Operation for Two Strings

# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

# In one step, you can delete exactly one character in either string.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for c in range(N+1):
            dp[0][c] = c
        for r in range(M+1):
            dp[r][0] = r
        for r in range(1, M+1):
            for c in range(1, N+1):
                if word1[c-1]==word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1+min(dp[r-1][c],dp[r][c-1])
        return dp[-1][-1]

        # Solution 2
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (word1[i] == word2[j]))
        return m + n - 2 * dp[m][n]