# coding: utf8
"""
---------------------------------------------
    File Name: 103-binary-tree-zigzag-level-order-traversal
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
import collections
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        buffer = []
        if root:
            buffer.append((root, 1))
        ltorFlag = True
        while len(buffer) > 0:
            if not ltorFlag:
                bufferRtL = buffer[::-1]
                ltorFlag = True
            else:
                bufferRtL = buffer
                ltorFlag = False

            tempBuf = []
            for node, level in bufferRtL:
                if len(res) < level:
                    res.append([node.val])
                else:
                    res[level - 1].append(node.val)
            for node, level in buffer:
                if node.left:
                    tempBuf.append((node.left, level + 1))
                if node.right:
                    tempBuf.append((node.right, level + 1))
            buffer = tempBuf

        return res
solu = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(4)
p.left.right = TreeNode(3)
p.right.left = TreeNode(5)
assert solu.zigzagLevelOrder(p) == [[1], [4, 2], [3, 5]]
exit()

