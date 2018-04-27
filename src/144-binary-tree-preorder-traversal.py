# coding: utf8
"""
---------------------------------------------
    File Name: 144-binary-tree-preorder-traversal
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

from collections import deque
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        # que = deque()
        stack = []
        while True:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left

            if not stack:
                break
            node = stack.pop()
            root = node.right

        return result
solu = Solution()
root = None
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.left.left = TreeNode(21)
# root.right = TreeNode(3)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(32)
print(solu.preorderTraversal(root))



