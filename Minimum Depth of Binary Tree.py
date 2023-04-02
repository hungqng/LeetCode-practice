# 111. Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            if None in [root.left, root.right]:
                return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
            else:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1