# coding: utf8
"""
---------------------------------------------
    File Name: 100-same-tree
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q and p.val == q.val:
            if p.left is None and p.right is None and q.left is None and q.right is None:
                return True
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif p is None and q is None:
            return True
        else:
            return False


solu = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)
q.left.right = TreeNode(3)
assert solu.isSameTree(p, q) == False
p = TreeNode(1)
p.left = TreeNode(2)
q = TreeNode(1)
q.right = TreeNode(2)
assert solu.isSameTree(p, q) == False
p = TreeNode(1)
q = TreeNode(1)
assert solu.isSameTree(p, q) == True
p = None
q = None
assert solu.isSameTree(p, q) == True
