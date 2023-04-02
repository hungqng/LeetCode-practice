# 119. Pascal's Triangle II

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pas = [[1]]
        for i in range(1, rowIndex + 1):
            temp = [1 for _ in range(i + 1)]
            for j in range(1, len(temp) - 1):
                temp[j] = pas[-1][j] + pas[-1][j - 1]
            pas.append(temp)
        return pas[-1]
        
        # Optimized solution only use O(rowIndex) extra space
        # res = [1]
        # for i in range(1, rowIndex + 1):
        #     res.append(1)
        #     for j in range(len(res) - 2, 0, -1):
        #         res[j] += res[j - 1]
        # return res