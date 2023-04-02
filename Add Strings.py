# 415. Add Strings

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        
        if len(num1) > len(num2):
            temp = num1
            num1 = num2
            num2 = temp
            
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(len(num1)):
            addition = (ord(num1[i]) - 48) + (ord(num2[i]) - 48) + carry
            result += chr(addition % 10 + 48)
            carry = int(addition / 10)
            
        for i in range(len(num1), len(num2)):
             addition = ord(num2[i]) - 48 + carry
             result += chr(addition % 10 + 48)
             carry = int(addition / 10)
            
        if carry:
             result += chr(carry + 48)
             
        return result[::-1]

        # Solution 2
        # nums1 = list(num1)
        # nums2 = list(num2)
        # res, carry = [], 0

        # while nums1 or nums2:
        #     n1 = n2 = 0
        #     if nums1: n1 = ord(nums1.pop()) - ord('0')
        #     if nums2: n2 = ord(nums2.pop()) - ord('0')
            
        #     carry, remain = divmod(n1 + n2 + carry, 10)
        #     res.append(remain)
        
        # if carry:
        #     res.append(carry)
        # return ''.join(str(d) for d in res)[::-1]

        # Solution 3
        # N, M = len(num1), len(num2)
        # a, b = N - 1, M - 1
        # carry = 0
        # output = ""
        # while a >= 0 or b >= 0:
        #     i, j = 0, 0
        #     if a >= 0:
        #         i = ord(num1[a]) -48
        #         a -= 1
        #     if b >= 0:
        #         j = ord(num2[b]) - 48
        #         b -= 1
        #     tmp = i + j + carry
        #     if tmp > 9:
        #         carry = 1
        #     else:
        #         carry = 0
        #     output = str(tmp)[-1] + output
        # if carry:
        #     output = "1" + output
        # return output