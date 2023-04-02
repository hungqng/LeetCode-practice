# 704. Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

        # Solution 2
        # index = bisect.bisect_left(nums, target)
        # return index if index < len(nums) and nums[index] == target else -1

        # Solution 3 O(log n)
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] < target:
        #         l = mid + 1
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         return mid
        # return -1
