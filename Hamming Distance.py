# 461. Hamming Distance

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

        # Solution 2
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y
        
        # Solution 3
        res, t = 0, x^y
        while t:
            t, res = t & (t-1), res + 1
        return res