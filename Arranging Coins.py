# 441. Arranging Coins

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        
        while l <= r:
            mid = (l + r) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res

        # Solution 2
        return int((math.sqrt(8 * n + 1)-1)/2)

        # Solution 3
        return int((-1 + (1 + 8 * n)**0.5) // 2)