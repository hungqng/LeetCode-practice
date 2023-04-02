# 507. Perfect Number

# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in (6, 28, 496, 8128, 33550336)

        # Solution 2
        if num == 1:
            return False
        res = 1
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                res += i + num//i
        return res == num

        # Solution 3
        if num <= 0: return False
        ans, SQRT = 0, int(num ** 0.5)
        ans = sum(i + num//i for i in range(1, SQRT+1) if not num % i)
        if num == SQRT ** 2: ans -= SQRT
        return ans - num == num