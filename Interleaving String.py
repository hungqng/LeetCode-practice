# 97. Interleaving String

# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp(i, j): if s1[:i] and s2[:j] can form the s3[:i+j]
       
        @cache
        def dfs(i, j):
            if not i and not j:
                return True
            return any((i and s1[i-1] == s3[i+j-1] and dfs(i-1, j), 
                       j and s2[j-1] == s3[i+j-1] and dfs(i, j-1)))
        return  len(s1) + len(s2) == len(s3) and dfs(len(s1), len(s2))

        # Solution 2
        @lru_cache(None)
        def dp(i, j):
            if i == -1 and j == -1: return True
            return (j >= 0 and s2[j] == s3[i+j+1] and dp(i, j-1)) or (i >= 0 and s1[i] == s3[i+j+1] and dp(i-1,j))
        
        return len(s1) + len(s2) == len(s3) and dp(len(s1) - 1, len(s2) - 1)