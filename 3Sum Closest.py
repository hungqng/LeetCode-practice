# 16. 3Sum Closest

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result

        # Two pointer
    #     nums.sort()
    # res = sum(nums[:3])
    # for i in xrange(len(nums)):
    #     l, r = i+1, len(nums)-1
    #     while l < r:
    #         s = sum((nums[i], nums[l], nums[r]))
    #         if abs(s-target) < abs(res-target):
    #             res = s
    #         if s < target:
    #             l += 1
    #         elif s > target:
    #             r -= 1
    #         else: # break early 
    #             return res
    # return res