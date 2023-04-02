# 561. Array Partition

# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        sum = 0
        while i < len(nums) - 1:
            sum += nums[i]
            i += 2
        return sum