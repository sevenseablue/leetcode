# coding: utf8
"""
---------------------------------------------
    File Name: 617-merge-two-binary-trees
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
    def dfs(self, t1, t2, t3):
        if t1 and not t2:
            t3.val = t1.val
            if t1.left:
                t3.left = TreeNode(0)
                self.dfs(t1.left, None, t3.left)
            if t1.right:
                t3.right = TreeNode(0)
                self.dfs(t1.right, None, t3.right)
        elif not t1 and t2:
            t3.val = t2.val
            if t2.left:
                t3.left = TreeNode(0)
                self.dfs(None, t2.left, t3.left)
            if t2.right:
                t3.right = TreeNode(0)
                self.dfs(None, t2.right, t3.right)
        elif t1 and t2:
            t3.val = t1.val + t2.val
            if t1.left or t2.left:
                t3.left = TreeNode(0)
                self.dfs(t1.left, t2.left, t3.left)
            if t1.right or t2.right:
                t3.right = TreeNode(0)
                self.dfs(t1.right, t2.right, t3.right)


    def dfs(self, t1, t2, t3):
        if t1 or t2:
            t1v = t1.val if t1 else 0
            t2v = t2.val if t2 else 0
            t3.val = t1v + t2v
            t1l = t1.left if t1 and t1.left else None
            t2l = t2.left if t2 and t2.left else None
            t1r = t1.right if t1 and t1.right else None
            t2r = t2.right if t2 and t2.right else None
            if t1l or t2l:
                t3.left = TreeNode(0)
                self.dfs(t1l, t2l, t3.left)
            if t1r or t2r:
                t3.right = TreeNode(0)
                self.dfs(t1r, t2r, t3.right)

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        t3 = TreeNode(0)
        self.dfs(t1, t2, t3)
        return t3


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


codec = Codec()
rootstr = "1,3,2,5"
# rootstr = "1"
root = codec.deserialize(rootstr)
print(codec.serialize(root) == rootstr)
rootstr = "2,1,3,,4,,7"
# rootstr = ""
root2 = codec.deserialize(rootstr)
print(codec.serialize(root2) == rootstr)

solu = Solution()
print(codec.serialize(solu.mergeTrees(root, root2)))



