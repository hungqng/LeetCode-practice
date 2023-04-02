# 459. Repeated Substring Pattern

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        
        def pattern(n):
            for i in range(0, N-n, n):
                if s[i:i+n] != s[i+n:i+2*n]:
                    return False
            return True
        for j in range(1, N//2+1):
            if pattern(j):return True
        return False

        # Solution 2
        ds = (s+s)[1:-1]
        
        return s in ds