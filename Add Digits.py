# 258. Add Digits

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            temp = 0
            while num:
                temp += num % 10
                num //= 10
            num = temp
        return num

        # Solution 2
        # if num == 0 : return 0
        # if num % 9 == 0 : return 9
        # else : return (num % 9)