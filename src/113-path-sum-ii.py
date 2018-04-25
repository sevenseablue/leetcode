# coding: utf8
"""
---------------------------------------------
    File Name: 113-path-sum-ii
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


# # dfs iterate
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

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return []
        queue = collections.deque()
        queue.append((root, root.val, [root.val]))
        result = []

        while queue:
            node, cumu, track = queue.popleft()
            if node.left is None and node.right is None and cumu==sum:
                result.append(track)
            if node.left:
                trackl = track.copy()
                trackl.append(node.left.val)
                queue.append((node.left, cumu+node.left.val, trackl))
            if node.right:
                trackl = track.copy()
                trackl.append(node.right.val)
                queue.append((node.right, cumu+node.right.val, trackl))

        return result

# bfs
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

    def pathSum(self, root, sum):
        if not root:
            return []
        stack, track, result = [], [], []
        cumu = 0
        while True:
            while root:
                cumu += root.val
                track = track.copy()
                track.append(root.val)
                # print(root.val, cumu, track)
                stack.append((root, cumu, track))
                root = root.left
            if not stack:
                break
            node, cumu, track = stack.pop()

            if node.left is None and node.right is None and sum == cumu:
                # print(node.val, cumu)
                result.append(track)
            root = node.right
        return result

solu = Solution()
preorder = [5,4,11,7,2,8,13,4,5,1]
inorder = [7,11,2,4,5,13,8,5,4,1]
root = solu.buildTree(preorder, inorder)
print(solu.pathSum(root, 22))

