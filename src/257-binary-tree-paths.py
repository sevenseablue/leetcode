# coding: utf8
"""
---------------------------------------------
    File Name: 257-binary-tree-paths
    Description: 
    Author: wangdawei
    date:   2018/4/27
---------------------------------------------
    Change Activity: 
                    2018/4/27
---------------------------------------------    
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        stack, result = [], []
        cumu = []
        while True:
            while root:
                cumu = cumu.copy()
                cumu.append(root.val)
                stack.append((root, cumu))
                root = root.left
            if not stack:
                break
            node, cumu = stack.pop()
            if node.left is None and node.right is None:
                result.append(cumu)
            root = node.right
        return [ "->".join([str(n) for n in r]) for r in result]


solu = Solution()
# root = TreeNode(6)
# root.left = TreeNode(2)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(4)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)
# root.right = TreeNode(8)
# root.right.left = TreeNode(7)
root = None
print(solu.binaryTreePaths(root))