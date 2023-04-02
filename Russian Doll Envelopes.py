# 354. Russian Doll Envelopes

# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

# Note: You cannot rotate an envelope.

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        env = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        dp = []
        
        for w,h in env:
            i = bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
        return len(dp)

        # Solution 2
        nums = sorted(envelopes, key = lambda x: [x[0], -x[1]])    
        dp = [10**10] * (len(nums) + 1)
        for elem in nums: dp[bisect_left(dp, elem[1])] = elem[1]  
        return dp.index(10**10)