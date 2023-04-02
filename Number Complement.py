# 476. Number Complement

# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.

class Solution:
    def findComplement(self, num: int) -> int:
        # Flip bit
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num

        # Solution 2
        return num ^ ((1<<num.bit_length())-1)

        # Solution 3
        return num ^ ((2<<int(math.log(num, 2)))-1)