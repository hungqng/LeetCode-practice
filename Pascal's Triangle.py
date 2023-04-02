# 118. Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res