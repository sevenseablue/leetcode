# coding: utf8
"""
---------------------------------------------
    File Name: CodeC
    Description: 
    Author: wangdawei
    date:   2018/4/28
---------------------------------------------
    Change Activity: 
                    2018/4/28
---------------------------------------------    
"""


from collections import deque

from TreeNode import TreeNode


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
