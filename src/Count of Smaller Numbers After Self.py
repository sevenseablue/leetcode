# coding: utf8
"""
---------------------------------------------
    File Name: Count of Smaller Numbers After Self
    Description: 
    Author: wangdawei
    date:   2018/2/8
---------------------------------------------
    Change Activity: 
                    2018/2/8
---------------------------------------------    
"""



class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        cou = [0] * len(nums)
        bst = self.BST()
        for i in range(len(nums)-1, -1, -1):
            bst.insert(nums[i])
            cou[i] = bst.find(nums[i])

        return cou

        pass

    class BST(object):
        class BSTNode(object):
            def __init__(self, val):
                self.val = val
                self.count = 0
                self.left , self.right = None, None

        def __init__(self):
            self.root = None

        def insert(self, val):
            node = self.BSTNode(val)
            if not self.root:
                self.root = node
                return
            cur = self.root
            while cur:
                if val < cur.val:
                    cur.count += 1
                    if cur.left is None:
                        cur.left = node
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = node
                        break
                    else:
                        cur = cur.right

        def find(self, val):
            cur = self.root
            count= 0
            while cur:
                if val < cur.val:
                    cur = cur.left
                elif val > cur.val:
                    count += 1 + cur.count
                    cur = cur.right
                else:
                    return count + cur.count



nums = [5, 2, 6, 1]
solu = Solution()
print(solu.countSmaller(nums))

