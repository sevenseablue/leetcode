# coding: utf8
"""
---------------------------------------------
    File Name: 102-binary-tree-level-order-traversal
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        deq = collections.deque()
        if root:
            deq.append((root, 1))
        while len(deq) > 0:
            node, level = deq.popleft()
            if len(res) < level:
                res.append([node.val])
            else:
                res[level - 1].append(node.val)
            if node.left:
                deq.append((node.left, level + 1))
            if node.right:
                deq.append((node.right, level + 1))

        return res
solu = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.left.right = TreeNode(3)
assert solu.levelOrder(p) == [[1], [2], [3]]
exit()


