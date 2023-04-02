# 1780. Check if Number is a Sum of Powers of Three

# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

# An integer y is a power of three if there exists an integer x such that y == 3x.

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            else:
                n //= 3
        return True

        # Solution 2
        # while n > 1:
        #     n, r = divmod(n, 3)
        #     if r == 2: return False
        # return True