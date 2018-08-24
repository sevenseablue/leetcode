# coding: utf8
"""
---------------------------------------------
    File Name: 94-binary-tree-inorder-traversal
    Description: 
    Author: wangdawei
    date:   2018/4/23
---------------------------------------------
    Change Activity: 
                    2018/4/23
---------------------------------------------    
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversalRes(self, res, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return
        self.inorderTraversalRes(res, root.left)
        res.append(root.val)
        self.inorderTraversalRes(res, root.right)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorderTraversalRes(res, root)
        return res

class Solution:
    def inorderTraversal(self, root):
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

solu = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(solu.inorderTraversal(root))
