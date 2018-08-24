# coding: utf8
"""
---------------------------------------------
    File Name: 230-kth-smallest-element-in-a-bst
    Description: 
    Author: wangdawei
    date:   2018/4/27
---------------------------------------------
    Change Activity: 
                    2018/4/27
---------------------------------------------    
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root):
        if root:
            lnum = self.dfs(root.left)
            root.rank = lnum + 1
            # print(root.val, root.rank)
            rnum = self.dfs(root.right)
            return lnum + rnum + 1
        else:
            return 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.dfs(root)
        while root:
            if root.rank == k:
                return root.val
            elif root.rank < k:
                k = k - root.rank
                root = root.right
            else:
                root = root.left





root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(5)
# root.num = 0
solu = Solution()
for i in range(1, 6):
    print("#"*30)
    print(solu.kthSmallest(root, i))
