# coding: utf8
"""
---------------------------------------------
    File Name: 145-binary-tree-postorder-traversal
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        while True:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.right
            if not stack:
                break
            node = stack.pop()
            root = node.left

        return result[::-1]

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack,result = [],[]
        while True:
            while root:
                stack.append((root,False))
                root = root.left
            if not stack:
                break
            top,visited = stack.pop()
            if top.right is None or visited is True:
                result.append(top.val)
            else:
                stack.append((top,True))
                root = top.right
        return result

solu = Solution()
# root = None
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left = TreeNode(21)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(32)
print(solu.postorderTraversal(root))
