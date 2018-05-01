# -*- coding: utf-8 -*-
"""
__author__ = 'wangdawei'
__time__ = '18-4-29 下午8:27'
"""

from TreeNode import TreeNode
from CodeC import Codec
import numpy as np
class Solution:
    def dfs(self, nums):
        if nums:
            ind = np.argmax(nums)
            val = nums[ind]
            root = TreeNode(val)
            leftTree = self.dfs(nums[:ind])
            rightTree = self.dfs(nums[ind+1:])
            root.left = leftTree
            root.right = rightTree
            return root
        else:
            return None


    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.dfs(nums)
        return root

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        for num in nums:
            node = TreeNode(num)
            # the node less and before is the left tree of the cur node
            while stack and stack[-1].val < num:
                node.left = stack.pop()

            # the cur node is the right child of the node greater and before
            if stack:
                stack[-1].right = node

            # the stack maintains the tree of the cur biggest node to the cur node with the right-child relationship.
            stack.append(node)
        return stack[0] if nums else None

