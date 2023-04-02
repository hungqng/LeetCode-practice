# 566. Reshape the Matrix

# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        N, M = len(mat[0]), len(mat)
        T = r*c
        if N*M != T:
            return mat
        output = [[0 for _ in range(c)] for _ in range(r)]
        tmp = []
        for i in range(M):
            for j in range(N):
                tmp.append(mat[i][j])
        k = 0
        for i in range(r):
            for j in range(c):
                output[i][j] = tmp[k]
                k += 1
        return output

        # Solution 2
        N, M = len(mat[0]), len(mat)
        T = r*c
        if N*M != T:
            return mat
        output = [[0 for _ in range(c)] for _ in range(r)]

        k = 0
        for i in range(M):
            for j in range(N):
                output[k//c][k%c] = mat[i][j]
                k += 1
        return output