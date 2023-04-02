# 303. Range Sum Query - Immutable

# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

    # Solution 2
    # def __init__(self, nums: List[int]):
    #     self.accu = [0]
    #     for num in nums: 
    #         self.accu += [self.accu[-1] + num]

    # def sumRange(self, left: int, right: int) -> int:
    #     return self.accu[right + 1] - self.accu[left]