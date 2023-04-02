# 1423. Maximum Points You Can Obtain from Cards

# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        M = N - k
        total = sum(cardPoints)
        mn = s = sum(cardPoints[:M])
        
        for i in range(k):
            s -= cardPoints[i]
            s += cardPoints[i+M]
            mn = min(mn, s)
        return total - mn

        # Solution 2
        best = total = sum(cardPoints[:k])
        for i in range (k-1, -1, -1):
            total += cardPoints[i + len(cardPoints) - k] - cardPoints[i]
            best = max(best, total)
        return best