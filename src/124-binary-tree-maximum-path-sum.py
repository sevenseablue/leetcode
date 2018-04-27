# coding: utf8
"""
---------------------------------------------
    File Name: 124-binary-tree-maximum-path-sum
    Description: 
    Author: wangdawei
    date:   2018/4/26
---------------------------------------------
    Change Activity: 
                    2018/4/26
---------------------------------------------    
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.maxPS = -2**31-1
    def dfs(self, root):

        if root:
            lmax = self.dfs(root.left)
            rmax = self.dfs(root.right)
            self.maxPS = max(self.maxPS, max(lmax, rmax, lmax+rmax, 0) + root.val)
            return max(lmax, rmax, 0) + root.val
        else:
            return 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.maxPS

solu = Solution()
root = TreeNode(-1)
root.left = TreeNode(-2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(-5)
root.right.left.right = TreeNode(-6)
print(solu.maxPathSum(root))
