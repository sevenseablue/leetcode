# coding: utf8
"""
---------------------------------------------
    File Name: 98-validate-binary-search-tree
    Description: 
    Author: wangdawei
    date:   2018/4/24
---------------------------------------------
    Change Activity: 
                    2018/4/24
---------------------------------------------    
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inOrder(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = self.inOrder(root)
        if len(nodes) in {0, 1}:
            return True
        for i in range(1, len(nodes)):
            if nodes[i]<=nodes[i-1]:
                return False
        return True



solu = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
assert solu.isValidBST(root) == True