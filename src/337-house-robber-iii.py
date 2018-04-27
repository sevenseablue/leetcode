# coding: utf8
"""
---------------------------------------------
    File Name: 337-house-robber-iii
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
    def dfs(self, root):
        if root:
            hasl, notHasl = self.dfs(root.left)
            hasr, notHasr = self.dfs(root.right)
            return [root.val + notHasl + notHasr, max(hasl, notHasl) + max(hasr, notHasr)]
        else:
            return (0, 0)


    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))

solu = Solution()
root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(3)
# root.left.right = TreeNode(6)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)
# root.right = TreeNode(8)
# root.right.left = TreeNode(7)
print(solu.rob(root))


