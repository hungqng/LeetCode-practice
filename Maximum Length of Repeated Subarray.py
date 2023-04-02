# 718. Maximum Length of Repeated Subarray

# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        output = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                output = max(output, dp[i][j])
        return output