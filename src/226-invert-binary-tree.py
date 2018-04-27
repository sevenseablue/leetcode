# coding: utf8
"""
---------------------------------------------
    File Name: 226-invert-binary-tree
    Description: 
    Author: wangdawei
    date:   2018/4/26
---------------------------------------------
    Change Activity: 
                    2018/4/26
---------------------------------------------    
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            self.dfs(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        return root


root = TreeNode(2)
root.left = TreeNode(1)
root.left.right = TreeNode(4)
# root.left.left = TreeNode(21)
root.right = TreeNode(3)
# root.right.left = TreeNode(5)
root.right.right = TreeNode(32)
# root = None
solu = Solution()
print(solu.inorderTraversal(root))
solu.invertTree(root)
print(solu.inorderTraversal(root))



