# 462. Minimum Moves to Equal Array Elements II

# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

# In one move, you can increment or decrement an element of the array by 1.

# Test cases are designed so that the answer will fit in a 32-bit integer.

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len (nums)
        mid = n//2
        nums.sort ()
        res = 0
        for i in range (n):
            res = res + abs (nums [i] - nums [mid])
        return res

        # Solution 2
        n = len (nums)
        mid = sorted (nums) [n // 2]
        res = sum (abs (i - mid) for i in nums)
        return res

        # Solution 3
        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums) // 2))