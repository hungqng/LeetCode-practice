# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s

        # Solution 2
        # l, r = 0, len(s) - 1
        # while l < r:
        #     s[l], s[r] = s[r], s[l]
        #     l, r = l + 1, r -1

        # Solution 3
        # s.reverse()