# 395. Longest Substring with At Least K Repeating Characters

# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or n < k:
            return 0
        if k <= 1:
            return n
        
        count = Counter(s)
        
        l = 0
        while l < n and count[s[l]] >= k:
            l += 1
        if l >= n - 1:
            return l
        
        ls1 = self.longestSubstring(s[0:l], k)
        while l < n and count[s[l]] < k:
            l += 1
        ls2 = self.longestSubstring(s[l:], k) if l < n else 0
        return max(ls1, ls2)

        # Solution 2
        # for c in set(s):
        #     if s.count(c) < k:
        #         return max(self.longestSubstring(t, k) for t in s.split(c))
        # return len(s)