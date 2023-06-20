# 228. Summary Ranges

# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        start, cur, end = nums[0], nums[0], None
        output = []
        for n in nums[1:]:
            cur += 1
            if n == cur:
                end = n
            else:
                if not end:
                    output.append(str(start))
                else:
                    output.append(str(start) + "->" + str(end))
                start = n
                cur = n
                end = None
        if not end:
            output.append(str(start))
        else:
            output.append(str(start) + "->" + str(end))
        return output
    
    