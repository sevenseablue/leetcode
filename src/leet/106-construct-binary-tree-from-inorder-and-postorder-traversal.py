# coding: utf8
"""
---------------------------------------------
    File Name: 106-construct-binary-tree-from-inorder-and-postorder-traversal
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

class Solution:
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

    def buildTreeDict(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # print(preorder, inorder)
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        if len(inorder) == 1 and len(postorder) == 1:
            return TreeNode(postorder[0])
        root = TreeNode(postorder[-1])
        ind = inorder.index(postorder[-1])

        inorderleft = inorder[0:ind]
        postorderleft = postorder[0:ind]
        root.left = self.buildTree(inorderleft, postorderleft)

        inorderright = inorder[ind+1:]
        postorderright = postorder[ind:len(postorder)-1]
        root.right = self.buildTree(inorderright, postorderright)

        return root

    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # print(preorder, inorder)
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        if len(inorder) == 1 and len(postorder) == 1:
            return TreeNode(postorder[0])
        root = TreeNode(postorder[-1])
        ind = inorder.index(postorder[-1])

        inorderleft = inorder[0:ind]
        postorderleft = postorder[0:ind]
        root.left = self.buildTree(inorderleft, postorderleft)

        inorderright = inorder[ind+1:]
        postorderright = postorder[ind:len(postorder)-1]
        root.right = self.buildTree(inorderright, postorderright)

        return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

solu = Solution()
root = solu.buildTree(inorder, postorder)
root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
assert solu.isSameTree(root, root2)
res = solu.inOrder(root)
print(res)


inorder = [3,2,1]
postorder = [3,2,1]
root = solu.buildTree(inorder, postorder)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)
assert solu.isSameTree(root, root2)