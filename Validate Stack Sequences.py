# 946. Validate Stack Sequences

# Given two integer arrays pushed and popped each with distinct values, 
# return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, 
# or false otherwise.

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for j in pushed:
            stack.append(j)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return stack == []