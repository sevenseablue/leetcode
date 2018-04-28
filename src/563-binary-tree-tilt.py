# coding: utf8
"""
---------------------------------------------
    File Name: 563-binary-tree-tilt
    Description: 
    Author: wangdawei
    date:   2018/4/28
---------------------------------------------
    Change Activity: 
                    2018/4/28
---------------------------------------------    
"""

from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        que = deque()
        que.append(root)
        res = []
        while que:
            node = que.popleft()
            if not node:
                res.append("")
                continue
            res.append(str(node.val))
            que.append(node.left)
            que.append(node.right)
        lasti = len(res)
        for i in range(len(res)-1, -1, -1):
            if res[i] != "":
                lasti = i + 1
                break
        return ",".join(res[:lasti])


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        nodes = deque(data.split(","))
        que = deque()
        root = TreeNode(int(nodes.popleft()))
        que.append(root)
        while que:
            node = que.popleft()
            nodec1 = nodes.popleft() if nodes else ""
            nodec2 = nodes.popleft() if nodes else ""

            if nodec1 != "":
                node.left = TreeNode(int(nodec1))
                que.append(node.left)
            if nodec2 != "":
                node.right = TreeNode(int(nodec2))
                que.append(node.right)
        return root
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root):
        if root:
            leftsum = self.dfs(root.left)
            rightsum = self.dfs(root.right)
            self.tilt += abs(leftsum - rightsum)
            return leftsum + rightsum + root.val
        else:
            return 0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        self.dfs(root)
        return self.tilt

codec = Codec()
rootstr = ""
root = codec.deserialize(rootstr)
print(codec.serialize(root) == rootstr)
solu = Solution()

print(solu.findTilt(root))

