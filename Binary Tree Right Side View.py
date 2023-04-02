# 199. Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l = defaultdict(list)
        def dfs(node, h):
            if not node: return
            l[h].append(node.val)
            dfs(node.left, h+1)
            dfs(node.right, h+1)
        dfs(root, 0)
        return [v[-1] for k, v in l.items()]