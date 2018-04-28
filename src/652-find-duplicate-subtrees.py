# coding: utf8
"""
---------------------------------------------
    File Name: 652-find-duplicate-subtrees
    Description: 
    Author: wangdawei
    date:   2018/4/28
---------------------------------------------
    Change Activity: 
                    2018/4/28
---------------------------------------------    
"""

from TreeNode import TreeNode
from CodeC import Codec
# TLE TLE
class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def traverse(node):
            if node :
                if not node.right and not node.left:
                    return "%s" % (node.val)
                elif node.right:
                    return "%s(%s)(%s)" % (node.val, traverse(node.left), traverse(node.right))
                else:
                    return "%s(%s)" % (node.val, traverse(node.left))
            else:
                return ""
        return traverse(t)

    def isSame(self, s, t):
        if s and t:
            if s.val == t.val:
                return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
            else:
                return False
        elif not s and not t:
            return True
        else:
            return False

    def dfs(self, s, t):
        if s:
            if self.isSame(s, t):
                return 1
            leftsame = self.dfs(s.left, t)
            rightsame = self.dfs(s.right, t)
            return leftsame + rightsame
        return 0


    def dfsallsub(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t:
            if self.dfs(s, t) > 1:
                self.__result.append(t)
            self.dfsallsub(s, t.left)
            self.dfsallsub(s, t.right)

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        s = root
        t = root
        self.__result = []
        self.dfsallsub(s, t)
        treestrset=set([])
        result = []
        for tree in self.__result:
            treestr = self.tree2str(tree)
            if treestr not in treestrset:
                result.append(tree)
            treestrset.add(treestr)
        return result


class Solution:
    def findDuplicateSubtrees(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return []
        stack = []
        root = t
        treestrdic = {}
        result = []
        while True:
            while root:
                stack.append((root, False))
                root = root.left
            if not stack:
                break
            node, visited = stack.pop()
            if visited:
                if not node.left and not node.right:
                    node.__str = "%s" % node.val
                elif node.left and not node.right:
                    node.__str = "%s(%s)" % (node.val, node.left.__str)
                elif not node.left and node.right:
                    node.__str = "%s()(%s)" % (node.val, node.right.__str)
                else:
                    node.__str = "%s(%s)(%s)" % (node.val, node.left.__str, node.right.__str)
                treestrdic[node.__str] = treestrdic.get(node.__str, 0) + 1
                if treestrdic.get(node.__str) == 2:
                    result.append(node)

            else:
                stack.append((node, True))
                root = node.right

        return result


codec = Codec()
rootstr = "4,2,3,4,,2,4,,,4"
root = codec.deserialize(rootstr)
print(codec.serialize(root) == rootstr)

solu = Solution()
for tree in solu.findDuplicateSubtrees(root):
    print(codec.serialize(tree))

