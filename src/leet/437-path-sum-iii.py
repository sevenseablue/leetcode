# coding: utf8
"""
---------------------------------------------
    File Name: 437-path-sum-iii
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

from collections import deque
class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        que = deque()
        result = 0
        que.append((root, [root.val]))
        while que:
            node, numList = que.popleft()
            for num in numList:
                if num == sum:
                    result += 1
            if node.left:
                numTmp = [e+node.left.val for e in numList]
                numTmp.append(node.left.val)
                que.append((node.left, numTmp))
            if node.right:
                numTmp = [e + node.right.val for e in numList]
                numTmp.append(node.right.val)
                que.append((node.right, numTmp))
        return result




class Solution:
    def pathSum(self, root, total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        self.ans = 0
        self.dfs(root, total, 0, {0: 1})
        return self.ans

    def dfs(self, root, target, currSum, preSum):
        if not root:
            return

        currSum += root.val
        complement = currSum - target
        self.ans += preSum.get(complement, 0)

        preSum[currSum] = preSum.get(currSum, 0) + 1

        self.dfs(root.left, target, currSum, preSum)
        self.dfs(root.right, target, currSum, preSum)

        preSum[currSum] -= 1



class Solution:
    def pathSum(self, root, total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        preSum = {0:1}
        curSum = 0
        res = 0
        stack = []
        while True:
            while root:
                curSum += root.val
                complement = curSum - total
                res += preSum.get(complement, 0)
                preSum[curSum] = preSum.get(curSum, 0) + 1
                stack.append((root, False))
                root = root.left
            if not stack:
                break
            node, visited = stack.pop()
            if visited:
                preSum[curSum] -= 1
                curSum -= node.val
            else:
                stack.append((node, True))
                root = node.right

        return res


import time
t1 = time.time()
root = TreeNode(-1)
cur = root
for i in range(2000):
    cur.left = TreeNode(i)
    cur = cur.left

# root = TreeNode(10)
# root.left = TreeNode(5)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(3)
# root.left.left.right = TreeNode(-2)
# root.left.right = TreeNode(2)
# root.left.right.right = TreeNode(1)
# root.right = TreeNode(-3)
# root.right.right = TreeNode(11)

solu = Solution()
print(solu.pathSum(root, 4))
print(time.time()-t1)



