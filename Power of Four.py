# 342. Power of Four

# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n != 0 and n &(n-1) == 0 and n & 1431655765 == n

        # Solution 2
        # if n == 1:
        #     return True 
        # if n%4 == 0:
        #     return ((n-1 & n) == 0) and (n%10 == 4 or n%10 == 6)
        # return False