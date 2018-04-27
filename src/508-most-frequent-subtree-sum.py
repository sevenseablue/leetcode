# coding: utf8
"""
---------------------------------------------
    File Name: 508-most-frequent-subtree-sum
    Description: 
    Author: wangdawei
    date:   2018/4/27
---------------------------------------------
    Change Activity: 
                    2018/4/27
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
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def subtreeSum(self, node):
        if node is None:
            return 0
        elif hasattr(node, 'num'):
            return node.num
        else:
            # print("recur")
            node.num = self.subtreeSum(node.left) + self.subtreeSum(node.right) + node.val
            return node.num
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        numDict = {}
        while True:
            while root:
                stack.append((root, False))
                root = root.left
            if not stack:
                break
            node, visited = stack.pop()
            if visited:
                # print(node.val)
                num = self.subtreeSum(node)
                numDict[num] = numDict.get(num, 0) + 1
            else:
                stack.append((node, True))
                root = node.right
        maxV=0
        result = []
        for k, v in numDict.items():
            if maxV < v:
                maxV = v
                result = []
                result.append(k)
            elif maxV == v:
                result.append(k)
        return result

codec = Codec()
root = codec.deserialize("5,2,-3")

print(codec.serialize(root))
solu = Solution()
print(solu.findFrequentTreeSum(root))


