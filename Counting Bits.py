# 338. Counting Bits

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

        # Solution 2
        # counter = [0]
        # for i in range(1, n+1):
        #     counter.append(counter[i >> 1] + i % 2)
        # return counter