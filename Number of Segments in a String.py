# 434. Number of Segments in a String

# Given a string s, return the number of segments in the string.

# A segment is defined to be a contiguous sequence of non-space characters.

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

        # Solution 2 not using split
        if len(s.strip()) < 1:
            return 0
        
        count = 0
        for i in range(len(s.strip()) - 1):
            if s[i] == " " and s[i + 1] != " " :
                count += 1
        return count + 1