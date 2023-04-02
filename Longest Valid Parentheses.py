# 32. Longest Valid Parentheses

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        mx = 0
        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mx = max(mx, i - stack[-1])
        return mx