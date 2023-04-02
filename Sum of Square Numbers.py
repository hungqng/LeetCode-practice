# 633. Sum of Square Numbers

# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq = int(sqrt(c))
        
        for a in range(sq + 1):
            b = sqrt(c - (a * a))
            if b == int(b): return True
        return False