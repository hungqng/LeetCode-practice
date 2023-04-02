# 99. Recover Binary Search Tree

# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.temp = []
        
        def dfs(node):
            if not node: return
            
            dfs(node.left)
            self.temp.append(node)
            dfs(node.right)
            
        dfs(root)
        
        srt = sorted(n.val for n in self.temp)
        
        for i in range(len(srt)):
            self.temp[i].val = srt[i]
            