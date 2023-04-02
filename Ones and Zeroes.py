# 474. Ones and Zeroes

# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for s in strs:
            ones = s.count("1")
            zeroes = s.count("0")
            for i in range(n, ones - 1, -1):
                for j in range(m, zeroes - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - ones][j - zeroes] + 1)
        return dp[n][m]