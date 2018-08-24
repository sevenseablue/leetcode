# coding: utf8
"""
---------------------------------------------
    File Name: 538-convert-bst-to-greater-tree
    Description: 
    Author: wangdawei
    date:   2018/4/27
---------------------------------------------
    Change Activity: 
                    2018/4/27
---------------------------------------------    
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        rootold = root
        stack = []
        cumu = 0
        while True:
            while root:
                stack.append(root)
                root = root.right
            if not stack:
                break
            node = stack.pop()
            cumu += node.val
            node.val = cumu
            root = node.left
        return rootold

