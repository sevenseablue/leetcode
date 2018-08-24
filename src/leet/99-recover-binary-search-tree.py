# coding: utf8
"""
---------------------------------------------
    File Name: 99-recover-binary-search-tree
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
            res.append(node)
            root = node.right

        return res

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = self.inOrder(root)
        rtol, ltor = -1, -1
        for i in range(1, len(res)):
            if res[i].val <= res[i-1].val:
                rtol = i-1
                break
        for i in range(len(res)-2, -1, -1):
            if res[i].val >= res[i+1].val:
                ltor = i+1
                break
        # print(ltor, rtol)
        temp = res[ltor].val
        res[ltor].val = res[rtol].val
        res[rtol].val = temp

solu = Solution()
root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)
root = TreeNode(3)
root.left=TreeNode(4)
res=solu.inOrder(root)
for n in res:
    print(n.val)
solu.recoverTree(root)
res=solu.inOrder(root)
for n in res:
    print(n.val)
