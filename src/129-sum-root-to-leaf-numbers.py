# coding: utf8
"""
---------------------------------------------
    File Name: 129-sum-root-to-leaf-numbers
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

from functools import reduce
class Solution(object):
    def __init__(self):
        self.path = []
        self.result = []
    def dfs(self, root):
        if root:
            self.path.append(root.val)
            if root.left is None and root.right is None:
                self.result.append(self.path.copy())
            self.dfs(root.left)
            self.dfs(root.right)
            self.path.pop()

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root)
        # print(self.result )
        # cumu = 0
        # for p in self.result:
        #     temp = 0
        #     for e in p:
        #         temp = temp*10 + e
        #     cumu += temp
        # print(cumu)
        # assert cumu == sum([reduce(lambda x, y: x*10 +y, p) for p in self.result])
        # print(sum([reduce(lambda x, y: x*10 +y, p) for p in self.result]))
        return sum([reduce(lambda x, y: x*10 +y, p) for p in self.result])

solu = Solution()
root = None
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
print(solu.sumNumbers(root))



