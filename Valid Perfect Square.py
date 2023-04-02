# 367. Valid Perfect Square

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x,i=0,1
        while x<num:
            x+=i
            i+=2
        return x==num

        # Solution 2 Newton's method
        # r = num
        # while r*r > num:
        #     r = (r + num/r) // 2
        # return r*r == num

        # Solution 3 Brute force O(sqrt(n))
        # for i in range(1, num + 1):
        #     if i * i == num:
        #         return True
        #     elif i * i > num:
        #         return False

        # Solution 4 Binary search O(log(n))
        # l, r = 1, num
        # while l <= r:
        #     mid = (l + r) // 2
        #     if mid * mid > num:
        #         r = mid - 1
        #     elif mid * mid < num:
        #         l = mid + 1
        #     else:
        #         return True
        # return False

        # Solution 5 Linear
        # i = 1
        # while i ** 2 <= num:
        #     if i ** 2 == num:
        #         return True
        #     else:
        #         i += 1
        # return False