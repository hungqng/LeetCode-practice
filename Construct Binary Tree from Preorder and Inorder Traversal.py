# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p = deque(preorder)
        N = len(preorder)
        lookup = {v:i for i, v in enumerate(inorder)}
        def rec(start, end):
            if start > end:
                return None
            else:
                cand = p.popleft()
                root = TreeNode(cand)
                middle = lookup[cand]
                root.left = rec(start, middle-1)
                root.right = rec(middle+1, end)
                return root
        return rec(0, N-1)

        # Solution 2
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root