# 763. Partition Labels

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        
        for i, c in enumerate(s):
            lastIndex[c] = i
            
        res = []
        size, end = 0, 0
        
        for i, c in enumerate(s):
            size += 1             
            end = max(end, lastIndex[c])
            
            if i == end:
                res.append(size)
                size = 0
        return res

        # Solution #2

        # L = len(s)
        # last = {s[i]: i for i in range(L)} # last appearance of the letter
        # i, ans = 0, []
        # while i < L:
        #     end, j = last[s[i]], i + 1
        #     while j < end: # validation of the part [i, end]
        #         if last[s[j]] > end:
        #             end = last[s[j]] # extend the part
        #         j += 1
        #     ans.append(end - i + 1)
        #     i = end + 1
            
        # return ans