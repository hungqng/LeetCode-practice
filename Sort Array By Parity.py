
# 905. Sort Array By Parity

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x % 2)
        return nums

        # Solution 2
        # output = []
        # for a in nums:
        #     if a % 2 == 0:
        #         output.insert(0, a)
        #     else:
        #         output.append(a)
        # return output

        # Solution 3
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     if nums[i] % 2 > nums[j] % 2:
        #         nums[i], nums[j] = nums[j], nums[i]
        #     if nums[i] % 2 == 0: i += 1
        #     if nums[j] % 2 == 0: j -= 1
        # return nums