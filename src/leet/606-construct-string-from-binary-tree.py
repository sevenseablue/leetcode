# coding: utf8
"""
---------------------------------------------
    File Name: 606-construct-string-from-binary-tree
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
class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        stack = []
        root = t
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
            else:
                stack.append((node, True))
                root = node.right

        return t.__str

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

codec = Codec()
# rootstr = "1,2,3,,4"
rootstr = "1"
root = codec.deserialize(rootstr)
print(codec.serialize(root) == rootstr)
# rootstr = "4,1,2"
# # rootstr = ""
# root2 = codec.deserialize(rootstr)
# print(codec.serialize(root2) == rootstr)

solu = Solution()
print(solu.tree2str(root))