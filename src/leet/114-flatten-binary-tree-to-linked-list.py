# coding: utf8
"""
---------------------------------------------
    File Name: 114-flatten-binary-tree-to-linked-list
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
# # dfs iterate
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

    def flatten(self, root):
        if root:
            self.flatten(root.left)
            self.flatten(root.right)
            if root.left and not root.right:
                root.right = root.left
                root.left = None
            elif root.right and root.left:
                recur = root.left
                while recur.right:
                    recur = recur.right
                recur.right = root.right
                root.right = root.left
                root.left = None



solu = Solution()
root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
solu.flatten(root2)
print(solu.levelOrder(root2))
print("#"*30)


preorder = [5,4,11,7,2,8,13,4,5,1]
inorder = [7,11,2,4,5,13,8,5,4,1]
root = solu.buildTree(preorder, inorder)
solu.flatten(root)
print(solu.levelOrder(root))


