# -*- coding: utf-8 -*-
"""
__author__ = 'wangdawei'
__time__ = '18-4-23 下午9:58'
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        last = stack.pop()
        res.append(last.val)
        root = last.right

    return res

class Solution:
    def generateTreesSE(self, s, e):
        if s == e:
            return [TreeNode(s)]
        if s > e:
            return [None]
        res = []
        for i in range(s, e+1):

            leftTrees = self.generateTreesSE(s, i-1)
            rightTrees = self.generateTreesSE(i+1, e)
            for lt in leftTrees:
                for rt in rightTrees:
                    root = TreeNode(i)
                    root.left = lt
                    root.right = rt
                    res.append(root)

        return res
        pass
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        return self.generateTreesSE(1, n)


solu = Solution()
trees = solu.generateTrees(2)
for t in trees:
    print(inorderTraversal(t))