# coding: utf8
"""
---------------------------------------------
    File Name: Serialize and Deserialize Binary Tree
    Description: 
    Author: wangdawei
    date:   2018/2/5
---------------------------------------------
    Change Activity: 
                    2018/2/5
---------------------------------------------    
"""

from queue import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # if root is None:
        #     return ""
        q = Queue(maxsize=0)
        q.put(root)
        serial_list = []
        while not q.empty():
            e = q.get()
            if e is not None:
                serial_list.append(str(e.val))
                q.put(e.left)
                q.put(e.right)
            else:
                serial_list.append(str(None))
            pass

        return ",".join(serial_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        e_li = data.split(",")
        print(e_li)
        e_li = [None if e == "None" else int(e) for e in e_li]
        if type(e_li[0]) != type(0):
            return None

        root = TreeNode(e_li[0])
        q = Queue(maxsize=0)
        q.put(root)
        cur_ind = 1
        while not q.empty() and cur_ind < len(e_li):
            e = q.get()
            if e_li[cur_ind] is not None:
                tn = TreeNode(e_li[cur_ind])
                e.left = tn
                q.put(tn)
            if e_li[cur_ind+1] is not None:
                tn = TreeNode(e_li[cur_ind+1])
                e.right = tn
                q.put(tn)
            cur_ind += 2

        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


root = TreeNode(1)
# e2 = TreeNode(2)
e3 = TreeNode(3)
# root.left = e2
root.right = e3
e4 = TreeNode(4)
# e5 = TreeNode(5)
e3.left = e4
# e3.right = e5

codec = Codec()
print(codec.serialize(root))
print(codec.serialize(codec.deserialize(codec.serialize(root))))

