# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        # Solution 2
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        sofar, output = 1, 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                sofar += 1
            else:
                sofar = 1
            output = max(output,sofar)
        return output