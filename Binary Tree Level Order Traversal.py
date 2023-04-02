# 102. Binary Tree Level Order Traversal

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #dfs
        output = []
        def dfs(node, level):
            if not node: return
            if len(output) < level+1:
                output.append([])
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            output[level].append(node.val)
        dfs(root, 0)
        return output
        
        #bfs
        q = deque([(root,0)])
        output, temp, prev_level = [], [], 0
        while q:
            node, level = q.popleft()
            if node:
                if level != prev_level:
                    output.append(temp)
                    temp = []
                    prev_level = level
                temp += [node.val]
                q.append((node.left, level + 1))
                q.append((node.right,level + 1))
        if temp:
            output.append(temp)
        return output