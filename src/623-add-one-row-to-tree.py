# coding: utf8
"""
---------------------------------------------
    File Name: 623-add-one-row-to-tree
    Description: 
    Author: wangdawei
    date:   2018/4/28
---------------------------------------------
    Change Activity: 
                    2018/4/28
---------------------------------------------    
"""

from TreeNode import TreeNode
from CodeC import Codec
from collections import deque
class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        que = deque()
        level = 1
        que.append((root, level))
        while que:
            node, level = que.popleft()
            print(node.val, level)
            if level == d - 1:
                print("go")
                # if node.left:
                nodeadd = TreeNode(v)
                nodeadd.left = node.left
                node.left = nodeadd
                # if node.right:
                nodeadd = TreeNode(v)
                nodeadd.right = node.right
                node.right = nodeadd

            if level < d - 1:
                if node.left:
                    que.append((node.left, level + 1))
                if node.right:
                    que.append((node.right, level + 1))

        return root
codec = Codec()
rootstr = "4,2,6,3,1,5"
rootstr = "4,2,,3,1"
rootstr = "1,2,3,4"
# rootstr = "1"
root = codec.deserialize(rootstr)
print(codec.serialize(root) == rootstr)
rootstr = "2,1,3,,4,,7"
# rootstr = ""
root2 = codec.deserialize(rootstr)
print(codec.serialize(root2) == rootstr)

solu = Solution()
print(codec.serialize(solu.addOneRow(root, 5, 4)))

