# coding: utf8
"""
---------------------------------------------
    File Name: 450-delete-node-in-a-bst
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
    def find(self, root, key):
        while root:
            if root.val == key:
                return root
            elif root.val > key:
                root = root.right
            else:
                root = root.left
        return None

    def findMax(self, root):
        while root:
            if root.right:
                root = root.right
            else:
                return root
        return None

    def findMin(self, root):
        while root:
            if root.left:
                root = root.left
            else:
                return root
        return None

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        rootold = root
        flag = False
        info = (None, None)
        while root:
            # print(root.val)
            if root.val == key:
                # print("delete")
                flag = True
                parent, ind = info
                if root.left and not root.right:
                    replace = root.left
                elif root.right and not root.left:
                    replace = root.right
                elif not root.left and not root.right:
                    replace = None
                else:
                    leftmax = self.findMax(root.left)
                    if leftmax != root.left:
                        self.deleteNode(root.left, leftmax.val)
                        leftmax.left = root.left
                    leftmax.right = root.right
                    replace = leftmax
                if parent is not None:
                    if ind == 1:
                        parent.left = replace
                    else:
                        parent.right = replace
                else:
                    rootold = replace
                return rootold
            elif root.val < key:
                info = (root, 2)
                root = root.right
            else:
                info = (root, 1)
                root = root.left


        return rootold



codec = Codec()
root = codec.deserialize("5,3,6,2,4,,7")

print(codec.serialize(root))
solu = Solution()
print(codec.serialize(solu.deleteNode(root, 0)))

