# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res

        # Solution 2
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)

        # Solution 3
        total = 0
        for i in range(len(nums) + 1):
            total += i
        return total - sum(nums)