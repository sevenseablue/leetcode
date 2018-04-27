# coding: utf8
"""
---------------------------------------------
    File Name: 404-sum-of-left-leaves
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        flag = False
        result = 0
        while True:
            while root:
                stack.append((root, flag))
                root = root.left
                flag = True
            if not stack:
                break
            node, leftF = stack.pop()
            if node.left is None and node.right is None and leftF:
                result += node.val
            root = node.right
            flag = False
        return result

solu = Solution()
root = TreeNode(4)
# root.left = TreeNode(1)
# root.left.left = TreeNode(2)
# root.left.left.left = TreeNode(3)
# root.left.right = TreeNode(6)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)
# root.right = TreeNode(8)
# root.right.left = TreeNode(7)
print(solu.sumOfLeftLeaves(root))

