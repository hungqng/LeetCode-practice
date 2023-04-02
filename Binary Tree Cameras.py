# 968. Binary Tree Cameras

# You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

# Return the minimum number of cameras needed to monitor all nodes of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.output =0
        def dfs(node):
            if not node:
                return False,True # camera, monitor
            c1, m1 = dfs(node.left)
            c2, m2 = dfs(node.right)
            
            camera, monitor = False, False
            if c1 or c2:
                monitor = True
            if not m1 or not m2:
                camera = True
                self.output += 1
                monitor = True
            return camera, monitor
        c, m = dfs(root)
        if not m:
            return self.output + 1
        return self.output

        # Solution 2
        self.output =0
        def dfs(root):
            if not root:
                return 2 # camera, monitor
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.output += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        return (dfs(root) == 0) + self.output

        # Solution 3
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            val = dfs(node.left) + dfs(node.right)
            if val == 0:
                return 3
            if val < 3:
                return 0
            self.ans += 1
            return 1
        return self.ans + 1 if dfs(root) > 2 else self.ans