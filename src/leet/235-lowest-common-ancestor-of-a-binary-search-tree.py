# coding: utf8
"""
---------------------------------------------
    File Name: 235-lowest-common-ancestor-of-a-binary-search-tree
    Description: 
    Author: wangdawei
    date:   2018/4/27
---------------------------------------------
    Change Activity: 
                    2018/4/27
---------------------------------------------    
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchOneStep(self, rootp, p):
        found = False
        if rootp.val == p.val:
            rootp = rootp
            found = True
        elif rootp.val > p.val:
            rootp = rootp.left
        elif rootp.val < p.val:
            rootp = rootp.right
        return rootp, found

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        rootp = root
        rootq = root
        lastancestor = root
        while True:
            rootp, foundp = self.searchOneStep(rootp, p)
            rootq, foundq = self.searchOneStep(rootq, q)

            if rootp != rootq:
                return lastancestor
            elif foundp:
                return rootp
            elif foundq:
                return rootq
            else:
                lastancestor = rootp


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
                # return self.lowestCommonAncestor(root.right, p, q)
            elif p.val < root.val and q.val < root.val:
                root = root.left
                # return self.lowestCommonAncestor(root.left, p, q)
            else:
                return root

        return None


solu = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
print(solu.lowestCommonAncestor(root, root.left.left, root.left.left).val)
