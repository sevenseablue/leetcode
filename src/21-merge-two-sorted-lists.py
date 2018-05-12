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
    def printLinkedList(self, head):
        while head:
            print(head.val)
            head = head.next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, tail = None, None
        while l1 and l2:
            if l1.val > l2.val:
                temp = l1
                l1 = l2
                l2 = temp
            if not head:
                head = l1
            else:
                tail.next = l1
            tail = l1
            l1 = l1.next
        if l2:
            l1 = l2
        if l1:
            if not head:
                head = l1
            else:
                tail.next = l1


        return head


l1 = None  # ListNode(0)
# l1.next = ListNode(4)
l2 = None  # ListNode(1)
# l2.next = ListNode(2)
solu = Solution()
h = solu.mergeTwoLists(l1, l2)
solu.printLinkedList(h)


