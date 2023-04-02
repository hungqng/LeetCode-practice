# 590. N-ary Tree Postorder Traversal

# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # postorder traversal method
        if root is None:
            return []
        result = []
        for child in root.children:
            result.extend(self.postorder(child))
        result.append(root.val)
        return result
        
        # preorder traversal method
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children)
        return result[::-1]