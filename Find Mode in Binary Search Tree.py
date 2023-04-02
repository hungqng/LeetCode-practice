# 501. Find Mode in Binary Search Tree

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []                            # result
        dic = {}                            # put node value in dictionary
        maxi = 0                            # the frequence of the most frequently occurred element
        
        def find(root):
            if not root:                    # leaf node
                return
            if root.val in dic:             # if node value is in the dictionry, value + 1
                dic[root.val] += 1
            else:
                dic[root.val] = 1           # if node value is not in the dictionary, value = 1
            find(root.left)
            find(root.right)
            return 
        
        find(root)
        dicval_list = list(dic.values())    # list all the values in dictionary
        maxi = max(dicval_list)             # find maximum value in dictionary
        
        for key, value in dic.items():
            if value == maxi:               # if value = maximum, append this key to list
                lst.append(key)
        return lst

        # Solution 2
    def helper(self, root, cache):
        if root == None:
            return
        cache[root.val] += 1
        self.helper(root.left, cache)
        self.helper(root.right, cache)
        return
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        cache = defaultdict(int)
        self.helper(root, cache)
        max_freq = max(cache.values())
        result = [k for k,v in cache.items() if v == max_freq]
        return result