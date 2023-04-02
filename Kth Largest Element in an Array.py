# 215. Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        return nums[k-1]

        # Solution 2
        return sorted(nums)[-k]