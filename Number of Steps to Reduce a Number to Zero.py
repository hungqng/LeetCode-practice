# 1342. Number of Steps to Reduce a Number to Zero

# Given an integer num, return the number of steps to reduce it to zero.

# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            counter += 1
        return counter

        # Solution 2
        digits = f'{num:b}'
        return digits.count('1') - 1 + len(digits)

        # Solution 3
        counter = num == 0
        while num > 0:
            counter += 1 + (num & 1)
            num >>= 1
        return counter - 1