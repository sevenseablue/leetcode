# coding: utf8
"""
---------------------------------------------
    File Name: Binary Tree Maximum Path Sum
    Description: 
    Author: wangdawei
    date:   2018/1/16
---------------------------------------------
    Change Activity: 
                    2018/1/16
---------------------------------------------    
"""

import sys



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.maxS = -sys.maxsize + 1
    def height(self, root):
        if root.left == None:
            l = 0
        else:
            l = self.height(root.left)
        if root.right == None:
            r = 0
        else:
            r = self.height(root.right)

        self.maxS = max(max(l, 0) + max(r, 0) + root.val, self.maxS)

        return max(l, r, 0) + root.val

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            self.height(root)
            return self.maxS

        pass

def main():

    root = TreeNode(-15)
    l = TreeNode(-2)
    l1 = TreeNode(-10)
    r1 = TreeNode(-21)
    r = TreeNode(-3)
    root.left = l
    root.right = r
    l.left = l1
    l.right = r1
    solu = Solution()
    print(solu.height(root))
    print(solu.maxPathSum(root))


if __name__ == "__main__":
    main()


