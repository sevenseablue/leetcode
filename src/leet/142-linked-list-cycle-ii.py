#!/home/wangdawei/anaconda2/envs/py3/bin/python 
# -*- coding: utf-8 -*-  
""" 
 @desc: 
 @author: wangdawei 
 @contact: 178129482@qq.com  
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        flag = False
        h1 = head
        h2 = head
        while h1 and h2 and h2.next:
            h1 = h1.next
            h2 = h2.next.next
            if h1 == h2:
                flag = True
                break
        if flag:
            h1 = head
            while h1 != h2:
                h1 = h1.next
                h2 = h2.next
            return h1
        return None

head = None
head = ListNode(0)
head.next = head
# head.next = ListNode(1)
# head.next.next = head.next
# head.next.next = ListNode(2)
# head.next.next.next = head.next
solu = Solution()
print(solu.detectCycle(head).val)



