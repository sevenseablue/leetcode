# coding: utf8
"""
---------------------------------------------
    File Name: 111-minimum-depth-of-binary-tree
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

# dfs recur
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

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return self.minDepth(root.right) + 1
        elif root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
# dfs recur
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

    def dfs(self, root):
        if root:
            # preorder
            self.pathcount += 1
            if root.left is None and root.right is None:
                if self.mindep > self.pathcount:
                    self.mindep = self.pathcount
            self.dfs(root.left)
            # inorder
            self.dfs(root.right)
            # postorder
            self.pathcount -= 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mindep = 2**31
        self.pathcount = 0
        if not root:
            return 0
        self.dfs(root)
        return self.mindep
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

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [[root]]
        level = 0
        while True:
            temp = []
            for i in stack[level]:
                if i.left is None and i.right is None:
                    return level + 1
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if not temp:
                break
            stack.append(temp)
            level += 1

# dfs iterate
import collections
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

    def minDepth(self, root):
        if not root:
            return 0
        que = collections.deque()
        level = 1
        mindep = 2**31
        while True:
            while root:
                que.append((root, level))
                root = root.left
                level += 1
            if not que:
                break
            node, level = que.pop()
            if node.left is None and node.right is None:
                if mindep > level:
                    mindep = level
            root = node.right
            level += 1
        return mindep



solu = Solution()
root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
print(solu.minDepth(root2))
print("#"*100)
preorder = [1,2,3,4,4,3,2]
inorder = [4,3,4,2,3,1,2]
root = solu.buildTree(preorder, inorder)
print(solu.minDepth(root))

