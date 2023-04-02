# 541. Reverse String II

# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)

        # Solution 2
        s = [s[i:i+k] for i in range(0, len(s), k)]
        for i in range(0, len(s), 2):
            s[i] = s[i][::-1]
        return ''.join(s)