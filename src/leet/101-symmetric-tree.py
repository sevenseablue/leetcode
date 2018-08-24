# coding: utf8
"""
---------------------------------------------
    File Name: 101-symmetric-tree
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
    def mirror(self, root):
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.mirror(root.left)
            self.mirror(root.right)

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

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or (root.left is None and root.right is None):
            return True
        self.mirror(root.left)
        return self.isSameTree(root.left, root.right)


solu = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.left.left = TreeNode(3)
p.right = TreeNode(2)
p.right.right = TreeNode(3)
assert solu.isSymmetric(p) == True
exit()
