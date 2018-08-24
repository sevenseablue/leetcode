# coding: utf8
"""
---------------------------------------------
    File Name: 112-path-sum
    Description: 
    Author: wangdawei
    date:   2018/4/25
---------------------------------------------
    Change Activity: 
                    2018/4/25
---------------------------------------------    
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
# bfs iterate
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # print(preorder, inorder)
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        ind = inorder.index(preorder[0])

        inorderleft = inorder[0:ind]
        preorderleft = preorder[1:1+ind]
        root.left = self.buildTree(preorderleft, inorderleft)

        inorderright = inorder[ind+1:]
        preorderright = preorder[ind+1:]
        root.right = self.buildTree(preorderright, inorderright)

        return root

    def hasPathSumLevelone(self, root, sum):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return False
        queue = [[(root, root.val)]]
        level = 0
        while True:
            temp = []
            for node, cumu in queue[level]:
                if node.left is None and node.right is None and cumu==sum:
                    return True
                if node.left:
                    temp.append((node.left, cumu+node.left.val))
                if node.right:
                    temp.append((node.right, cumu+node.right.val))
            if not temp:
                break
            queue.append(temp)
            level += 1
        return False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return False
        queue = collections.deque()
        queue.append((root, root.val))

        while queue:
            node, cumu = queue.popleft()
            if node.left is None and node.right is None and cumu==sum:
                return True
            if node.left:
                queue.append((node.left, cumu+node.left.val))
            if node.right:
                queue.append((node.right, cumu+node.right.val))

        return False

# dfs iterate
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # print(preorder, inorder)
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        ind = inorder.index(preorder[0])

        inorderleft = inorder[0:ind]
        preorderleft = preorder[1:1+ind]
        root.left = self.buildTree(preorderleft, inorderleft)

        inorderright = inorder[ind+1:]
        preorderright = preorder[ind+1:]
        root.right = self.buildTree(preorderright, inorderright)

        return root

    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack = []
        cumu = 0
        while True:
            while root:
                cumu += root.val
                stack.append((root, cumu))
                root = root.left
            if not stack:
                break
            node, cumu = stack.pop()
            # print(node.val, cumu)
            if node.left is None and node.right is None:
                if sum == cumu:
                    return True
            root = node.right
        return False

solu = Solution()
root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
print("#"*30)
print(solu.hasPathSum(root2, 12))
print("#"*30)
print(solu.hasPathSum(root2, 30))
print("#"*30)
print(solu.hasPathSum(root2, 38))
print("#"*30)
print(solu.hasPathSum(root2, 37))