# 504. Base 7

# Given an integer num, return a string of its base 7 representation.

class Solution:
    def convertToBase7(self, num: int) -> str:
        n, res = abs(num), ''
        while n:
            res = str(n % 7) + res
            n //= 7
        return '-' * (num < 0) + res or "0"