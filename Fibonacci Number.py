# 509. Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

        # Solution 2
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev1, prev2 = 1,0
        output = 0
        for i in range(2, n + 1):
            output = prev1 + prev2
            prev2 = prev1
            prev1 = output
        return output