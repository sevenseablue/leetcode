# coding: utf8
"""
---------------------------------------------
    File Name: 236-lowest-common-ancestor-of-a-binary-tree
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = []
        pa = []
        qa = []
        while True:
            while root:
                stack.append((root, False))
                root = root.left
            if not stack:
                break
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
            else:
                if node == p:
                    pa = [n for n, v in stack]
                    pa.append(p)
                if node == q:
                    qa = [n for n, v in stack]
                    qa.append(q)
                if pa and qa:
                    break
            root = node.right

        lastancestor = root
        for pe, qe in zip(pa, qa):
            if pe != qe:
                return lastancestor
            else:
                lastancestor = pe
        return lastancestor


solu = Solution()
root = TreeNode(6)
# root.left = TreeNode(2)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(4)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)
# root.right = TreeNode(8)
# root.right.left = TreeNode(7)
print(solu.lowestCommonAncestor(root, root, root).val)
