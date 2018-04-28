# coding: utf8
"""
---------------------------------------------
    File Name: 572-subtree-of-another-tree
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
    def isSame(self, s, t):
        if s and t:
            # print(s.val, t.val)
            if s.val == t.val:
                return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
            else:
                return False
        elif not s and not t:
            return True
        else:
            return False

    def dfs(self, s, t):
        if s and t:
            if self.isSame(s, t):
                self.__isSubtree = True
            if not self.__isSubtree:
                self.dfs(s.left, t)
            if not self.__isSubtree:
                self.dfs(s.right, t)
        elif not s and not t:
            self.__isSubtree = True
        else:
            self.__isSubtree = False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.__isSubtree = False
        self.dfs(s, t)
        return self.__isSubtree


class Solution:

    def isSubtree(self, s, t):
        def traverse(node):
            if node is None:
                return "^"
            else:
                return "$"+str(node.val)+"#"+traverse(node.left)+"@"+traverse(node.right)
        # print(traverse(t), traverse(s))
        return traverse(t) in traverse(s)

codec = Codec()
rootstr = "3,4,5,1,2,,,,0"
# rootstr = "1"
root = codec.deserialize(rootstr)
print(codec.serialize(root) == rootstr)
rootstr = "4,1,2"
# rootstr = ""
root2 = codec.deserialize(rootstr)
print(codec.serialize(root2) == rootstr)

solu = Solution()
print(solu.isSubtree(root, root2))