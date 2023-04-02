# 29. Divide Two Integers

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dv = abs(divisor)
        output = 0
        
        while d >= dv:
            tmp = dv
            mul = 1
            while d >= tmp:
                d -= tmp
                output += mul
                mul += mul
                tmp += tmp

        if dividend < 0 and divisor >= 0 or divisor < 0 and dividend >= 0:
            output = -output
        
        return min(2147483647, max(-2147483648, output))