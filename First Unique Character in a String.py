# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(list(s))
        for i in range(len(s)):
            if counter.get(s[i]) == 1:
                return i
        return -1

        # Solution 2
        # d = {}
        # seen = set()
        # for idx, c in enumerate(s):
        #     if c not in seen:
        #         d[c] = idx
        #         seen.add(c)
        #     elif c in d:
        #         del d[c]
        # return next(iter(d.values())) if d else -1