class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Solution 1 converting to string
        # return (str(x) == str(x)[::-1])

        # Solution 2:
        if x < 0:
            return False
        
        div = 1
        while x >= 10 * div:
            div *= 10
        
        while x != 0:
            right = x % 10
            left = x // div

            if left != right:
                return False
            x = (x % div) // 10
            div = div / 100
        return True

        # Solution 2
        # reverse = 0
        # num = x
        
        # while (num > 0):
        #     current = num % 10
        #     reverse = reverse * 10 + current
        #     num = num // 10
            
        # if reverse == x:
        #     return True
        # else:
        #     return False