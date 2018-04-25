# coding: utf8
"""
---------------------------------------------
    File Name: 116-populating-next-right-pointers-in-each-node
    Description: 
    Author: wangdawei
    date:   2018/4/25
---------------------------------------------
    Change Activity: 
                    2018/4/25
---------------------------------------------    
"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

import collections
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        que = collections.deque()
        if not root:
            return
        que.append((root, 1))
        lasttuple = (None, 0)
        while que:
            node, level = que.popleft()
            # print("node, level, {}, {}", node.val, level)
            if lasttuple[1] == level:
                lasttuple[0].next = node
                # print(lasttuple[0].val, node.val)
            lasttuple = (node, level)
            if node.left:
                que.append((node.left, level + 1))
            if node.right:
                que.append((node.right, level+1))
        pass


solu = Solution()
root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
root.left.left = TreeLinkNode(4)
root.left.right = TreeLinkNode(5)
root.right.left = TreeLinkNode(6)
# root.left.next = root.right
solu.connect(root)


