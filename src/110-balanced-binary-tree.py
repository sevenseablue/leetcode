# coding: utf8
"""
---------------------------------------------
    File Name: 110-balanced-binary-tree
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

class Solution:
    def __init__(self):
        self.nodeheight = {}
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
    def height(self, root):
        if root is None:
            return 0
        else:
            if root not in self.nodeheight:
                self.nodeheight[root] = max(self.height(root.left), self.height(root.right)) + 1
                return self.nodeheight[root]
            else:
                # print("root in dict: ", root.val)
                return self.nodeheight[root]
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            if abs(self.height(node.left) - self.height(node.right)) > 1:
                return False
            root = node.right
        return True

root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
solu = Solution()
print(solu.isBalanced(root2))

preorder = [1,2,3,4,4,3,2]
inorder = [4,3,4,2,3,1,2]
root = solu.buildTree(preorder, inorder)
print(solu.isBalanced(root))


