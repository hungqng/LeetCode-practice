# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    # Method 1 -- Apply hashtable O(n)
    # hashNum = {}
    # for i in nums:
    #     if i not in hashNum:
    #         hashNum[i] = 1
    #     else:
    #         return True
    # return False
    
    # Method 2 -- Sorting
    # l =  len(nums)
    # if l < 2:
    #     return False
    # nums.sort()
    # for i in range(l-1):
    #     if nums[i] == nums[i+1]:
    #         return True
    # return False