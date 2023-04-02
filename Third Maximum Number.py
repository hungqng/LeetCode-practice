# 414. Third Maximum Number

# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums)<=2:
            return nums[-1]
        return nums[-3]
        