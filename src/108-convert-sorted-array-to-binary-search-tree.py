# coding: utf8
"""
---------------------------------------------
    File Name: 108-convert-sorted-array-to-binary-search-tree
    Description: 
    Author: wangdawei
    date:   2018/4/24
---------------------------------------------
    Change Activity: 
                    2018/4/24
---------------------------------------------    
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        deq = collections.deque()
        if root:
            deq.append((root, 1))
        while len(deq) > 0:
            node, level = deq.popleft()
            if len(res) < level:
                res.append([node.val])
            else:
                res[level - 1].append(node.val)
            if node.left:
                deq.append((node.left, level + 1))
            if node.right:
                deq.append((node.right, level + 1))

        return res

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q and p.val == q.val:
            if p.left is None and p.right is None and q.left is None and q.right is None:
                return True
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif p is None and q is None:
            return True
        else:
            return False
    def inOrder(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums)>>1
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


nums = [-10,-3,0,5,9]
solu = Solution()
for i in range(len(nums)+1):
    root = solu.sortedArrayToBST(nums[:i])
    res = solu.levelOrder(root)
    print(res)

