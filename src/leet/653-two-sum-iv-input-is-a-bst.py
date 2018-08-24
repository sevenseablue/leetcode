# coding: utf8
"""
---------------------------------------------
    File Name: 653-two-sum-iv-input-is-a-bst
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
class Solution:

    def find(self, root, key):
        while root:
            if root.val == key:
                return root
            elif root.val > key:
                root = root.left
            else:
                root = root.right
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


    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        maxv = self.findMax(root).val
        minv = self.findMin(root).val
        if k >= 2*maxv or k<=2*minv:
            return False
        stack = []
        rootold = root
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            queryv = k - node.val
            if queryv != node.val and self.find(rootold, queryv) is not None:
                return True

            root = node.right

        return False

codec = Codec()
rootstr = "5,3,6,2,4,,7"
root = codec.deserialize(rootstr)
print(codec.serialize(root) == rootstr)

solu = Solution()
for i in range(8):
    print("#######################################")
    print(i, solu.findTarget(root, i))