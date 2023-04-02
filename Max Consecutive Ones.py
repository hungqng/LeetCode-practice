# 485. Max Consecutive Ones

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for num in nums:
            if num == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0
        return res

        # Solution 2
        return max(sum(g) for _, g in groupby(nums))