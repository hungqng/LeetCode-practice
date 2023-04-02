# 1049. Last Stone Weight II

# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the smallest possible weight of the left stone. If there are no stones left, return 0.

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        for a in stones:
            dp = {a + x for x in dp} | {abs(a - x) for x in dp}
        return min(dp)

        # Solution 2
        # dp = {0}
        # sumA = sum(stones)
        # for a in stones:
        #     dp |= {a + i for i in dp}
        # return min(abs(sumA - i - i) for i in dp)