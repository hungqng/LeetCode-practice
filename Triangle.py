# 120. Triangle

# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])
        
        return dp[0]

        # Solution 2 Recursion
        def dfs(i, j):
            if i == len(triangle):
                return 0
            lower_left = triangle[i][j] + dfs(i + 1, j)
            lower_right = triangle[i][j] + dfs(i + 1, j + 1)
            return min(lower_left, lower_right)
        return dfs(0,0)

        # Solution 3
        return reduce(lambda a,b:[f+min(d,e)for d,e,f in zip(a,a[1:],b)],triangle[::-1])[0]