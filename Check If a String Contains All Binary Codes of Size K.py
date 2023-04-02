# 1461. Check If a String Contains All Binary Codes of Size K

# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        dis_sub = 2**k
        N = len(s)
        tracker = set([s[i:i + k] for i in range(N + 1 - k)])
        
        return dis_sub == len(tracker)

        # Solution 2
        return len({s[i:i + k] for i in range(len(s) - k + 1)}) == 2 ** k