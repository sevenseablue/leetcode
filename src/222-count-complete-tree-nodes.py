# coding: utf8
"""
---------------------------------------------
    File Name: 222-count-complete-tree-nodes
    Description: 
    Author: wangdawei
    date:   2018/4/26
---------------------------------------------
    Change Activity: 
                    2018/4/26
---------------------------------------------    
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getheight(self, root):
        h = 0
        while root:
            root = root.left
            h += 1
        return h

    def checkExists(self, root, index):
        path = bin(self.upCumu + 1 + index)[3:]
        for p in path:
            if p == "0":
                root = root.left
            else:
                root = root.right
        if root is None:
            return False
        else:
            return True

    def checkStatus(self, root, index):
        return self.checkExists(root, index), self.checkExists(root, index + 1)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.height = self.getheight(root)
        if self.height == 0:
            return 0
        self.upCumu = 2 ** (self.height - 1) - 1
        l, r = 0, 2**(self.height - 1) - 1
        while l <= r:
            mid = (l + r) >> 1
            status = self.checkStatus(root, mid)
            if status == (True, False):
                return self.upCumu + mid + 1
            elif status == (True, True):
                l = mid + 1
            elif status == (False, False):
                r = mid -1
            else:
                raise "wrong input, not a complete tree."


class Solution:
    def findHeight(self, node):
        return -1 if node is None else 1 + self.findHeight(node.left)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.findHeight(root)
        return 0 if h == -1 else ((1 << h) + self.countNodes(root.right)  \
                                  if self.findHeight(root.right) == h - 1  \
                                  else (1 << h - 1) + self.countNodes(root.left))


class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        h = self.height(root)
        res = 0
        while root:
            if self.height(root.right) == h - 1:
                res += 1 << h
                root = root.right
            else:
                res += 1 << (h - 1)
                root = root.left
            h -= 1

        return res


    def height(self, node):
        if not node:
            return -1
        else:
            return 1 + self.height(node.left)


root = TreeNode(2)
root.left = TreeNode(1)
root.left.right = TreeNode(4)
root.left.left = TreeNode(21)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(32)
# root = None
solu = Solution()
print(solu.countNodes(root))
