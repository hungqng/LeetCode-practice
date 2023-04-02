# 101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.is_reverse(root.left, root.right)
        
        
    def is_reverse(self, a, b):
        # return true iff `a` is a reversed tree of `b`
        if not a or not b:
            return not a and not b
        return a.val == b.val and self.is_reverse(a.left,b.right) and self.is_reverse(a.right,b.left)      