# 59. Spiral Matrix II

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for r in range(n)]
        i = 0
        left, right = 0, n
        top, bottom = 0, n
        
        while left < right and top < bottom:
            # get every i in the top row
            for c in range(left, right):
                i += 1
                res[top][c] = i 
            top += 1
            
            # get every i in the right col
            for r in range(top, bottom):
                i += 1
                res[r][right - 1] = i
            right -= 1
            
            
            # get every in the bottom row
            for c in range(right - 1, left - 1, -1):
                i += 1
                res[bottom - 1][c] = i
            bottom -= 1
            
            # get every in the left col
            for r in range(bottom - 1, top - 1, -1):
                i += 1
                res[r][left] = i
            left += 1
            
        return res