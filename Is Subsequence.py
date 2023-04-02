# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return True if i == len(s) else False

        # Solution 2
        # t = iter(t)
        # return all(c in t for c in s)

        # Solution 3
        # remainder_of_t = iter(t)
        # for letter in s:
        #     if letter not in remainder_of_t:
        #         return False
        # return True