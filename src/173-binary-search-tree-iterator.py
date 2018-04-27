# coding: utf8
"""
---------------------------------------------
    File Name: 173-binary-search-tree-iterator
    Description: 
    Author: wangdawei
    date:   2018/4/26
---------------------------------------------
    Change Activity: 
                    2018/4/26
---------------------------------------------    
"""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        if self.root:
            self.__hasNext = True
        else:
            self.__hasNext = False
        self.g = self.iterate()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.__hasNext

    def iterate(self):
        stack = []
        root = self.root
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            root = node.right

            if root or stack:
                self.__hasNext = True
            else:
                self.__hasNext = False
            yield node.val

    def next(self):
        """
        :rtype: int
        """
        return next(self.g)

# class BSTIterator(object):
#   def __init__(self, root):
#     self.stack = []
#     self._extract(root)
#
#   def _extract(self, root):
#     while root:
#       self.stack.append(root)
#       root = root.left
#
#   def hasNext(self):
#     return len(self.stack) > 0
#
#   def next(self):
#     node = self.stack.pop()
#     if node.right:
#       self._extract(node.right)
#     return node.val
#
# class BSTIterator(object):
#     def __init__(self, root):
#         self.last = root
#         while self.last and self.last.right:
#             self.last = self.last.right
#         self.current = None
#         self.g = self.iterate(root)
#
#     # @return a boolean, whether we have a next smallest number
#     def hasNext(self):
#         return self.current is not self.last
#
#     # @return an integer, the next smallest number
#     def next(self):
#         return next(self.g)
#
#     def iterate(self, node):
#         if node is None:
#             return
#         for x in self.iterate(node.left):
#             yield x
#         self.current = node
#         yield node.val
#         for x in self.iterate(node.right):
#             yield x

root = TreeNode(2)
root.left = TreeNode(1)
# root.left.right = TreeNode(4)
# root.left.left = TreeNode(21)
root.right = TreeNode(3)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(32)
i, v = BSTIterator(root), []
while i.hasNext():
    val = i.next()
    print("has", val)

    v.append(val)
print(v)
