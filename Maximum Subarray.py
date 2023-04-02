# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for idx in range(1, len(nums)):
            if nums[idx-1] > 0:
                nums[idx] += nums[idx-1]
                
        return max(nums)

        # Solution 2
        # maxSub = nums[0]
        # curSum = 0
        
        # for n in nums:
        #     if curSum < 0:
        #         curSum = 0
        #     curSum += n
        #     maxSub = max(maxSub, curSum)
        # return maxSub