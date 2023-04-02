# 1658. Minimum Operations to Reduce X to Zero

# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        dp = [0]
        z = 0
        for n in nums:
            z += n
            dp.append(z)
        lookup = {v:i for i, v in enumerate(dp)}
        y = sum(nums) - x
        ans = -1
        for l_val, l_idx in lookup.items():
            if l_val + y in lookup:
                ans = max(lookup[l_val + y] - l_idx, ans)
        if ans == -1:
            return ans
        else:
            return len(nums)-ans

        # Solution 2
        cumsum = [0] + list(accumulate(nums))
        dic = {c:i for i,c in enumerate(cumsum)}
        goal = cumsum[-1] - x
        ans = -float("inf")

        if goal < 0: return -1

        for num in dic:
            if num + goal in dic:
                ans = max(ans, dic[num + goal] - dic[num])

        return len(nums) - ans if ans != -float("inf") else -1

        # Solution 3
        target, size, win_sum, lo, n = sum(nums) - x, -1, 0, -1, len(nums)
        for hi, num in enumerate(nums):
            win_sum += num
            while lo + 1< n and win_sum > target:
                lo += 1
                win_sum -= nums[lo]
            if win_sum == target:
                size = max(size, hi - lo)
        return -1 if size < 0 else n - size