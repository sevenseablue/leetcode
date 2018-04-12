# coding: utf8
"""
---------------------------------------------
    File Name: binary_tree_pruning
    Description: 
    Author: wangdawei
    date:   2018/4/11
---------------------------------------------
    Change Activity: 
                    2018/4/11
---------------------------------------------    
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left is None and root.right is None and root.val == 0:
            root = None

        return root


def buildTree(input):
    treeNodes = []
    for i in range(len(input)):
        if input[i] is not None:
            treeNodes.append(TreeNode(input[i]))
        else:
            treeNodes.append(None)
    if len(treeNodes) == 0:
        return None
    root = treeNodes[0]
    i, j = 0, 1
    l = len(treeNodes)
    while l > i and l > j:
        if treeNodes[i] != None:
            treeNodes[i].left = treeNodes[j]
            j += 1
            if l > j:
                treeNodes[i].right = treeNodes[j]
                j += 1
        i += 1
    return root



def printTree(root):
    que = [root]
    while len(que) > 0:
        cur = que.pop(0)
        if cur is not None:
            print(cur.val, end=", ")
            if not (cur.left is None and cur.right is None):
                # print(cur.val, cur.left.val if cur.left is not None else "None", cur.right.val if cur.right is not None else "None")
                que.append(cur.left)
                que.append(cur.right)
        else:
            print("None", end=", ")
            # print("None")
    print("")


for input in [
    [1, None, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 0],
    [0],
    [0, 0, ],
    [0, 0, 0],
    []
]:
    root = buildTree(input)
    printTree(root)
    solu = Solution()
    root = solu.pruneTree(root)
    printTree(root)
