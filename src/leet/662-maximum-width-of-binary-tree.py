# -*- coding: utf-8 -*-
"""
__author__ = 'wangdawei'
__time__ = '18-5-1 下午10:03'
"""

from TreeNode import TreeNode
from CodeC import Codec
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        que = deque()
        level = 0
        que.append((root, level, 0))
        curlevel = -1
        indmin, indmax = -1, -1
        widthmax = 0
        while que:
            node, level, ind = que.popleft()
            # print(node.val, level, ind, curlevel)
            if curlevel != level:
                indmin, indmax = ind, ind
            if ind > indmax:
                indmax = ind
            if widthmax < indmax - indmin + 1:
                widthmax = indmax - indmin + 1
            if node.left:
                que.append((node.left, level + 1, 2 * ind + 1))
            if node.right:
                que.append((node.right, level + 1, 2 * ind + 2))
            curlevel = level

        return widthmax

codec = Codec()
solu = Solution()
for rootstr in ["1,2,3,4", "", "1", "1,2,,4", "1,2,3,4,,,7",
                ]:
    root = codec.deserialize(rootstr)
    print(codec.serialize(root) == rootstr)
    print(solu.widthOfBinaryTree(root))
