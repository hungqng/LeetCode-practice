# 289. Game of Life

# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
 

# Follow up:

# Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        def countNeighbors(r, c):
            nei = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if ((i == r and j == c) or i < 0 or j < 0 or i == ROWS or j == COLS):
                        continue
                    if board[i][j] in [1, 3]:
                        nei += 1
            return nei
        
        for r in range(ROWS):
            for c in range(COLS):
                nei = countNeighbors(r, c)
                
                if board[r][c]:
                    if nei in [2, 3]:
                        board[r][c] = 3
                elif nei == 3:
                    board[r][c] = 2
                    
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1