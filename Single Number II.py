# 137. Single Number II

# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        for k, v in count.items():
            if v == 1:
                return k

        # Solution 2
        single = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1 << i) == (1 << i):
                    count += 1
            single |= (count % 3) << i
        return single if single < (1 << 31) else single - (1 << 32)