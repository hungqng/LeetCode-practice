# 1260. Shift 2D Grid

# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

# In one shift operation:

# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        
        def posToVal(r, c):
            return r * N + c
        def valToPos(v):
            return [v // N, v % N]
        
        res = [[0] * N for i in range(M)]
        for r in range(M):
            for c in range(N):
                newVal = (posToVal(r, c) + k) % (M * N)
                newR, newC = valToPos(newVal)
                res[newR][newC] = grid[r][c]
        return res