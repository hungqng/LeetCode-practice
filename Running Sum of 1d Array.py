# 1480. Running Sum of 1d Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            result.append(total)
        return result

        # Solution 2
        result = []
        result.append(nums[0])
        for i in range(1, len(nums)):
            result.append(result[-1]+nums[i])
        return result

        # Solution 3
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

        # Solution 4
        return [sum(nums[:i+1]) for i in range(len(nums))]

        # Solution 5
        return accumulate(nums)