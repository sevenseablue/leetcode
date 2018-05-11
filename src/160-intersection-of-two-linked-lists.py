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
    def arrayToList(self, list):
        if not list:
            return None
        head = ListNode(list[0])
        cur = head
        for i in range(1, len(list)):
            cur.next = ListNode(list[i])
            cur = cur.next

        return head

    def listToArray(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next

        return result

    def getListLen(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la = self.getListLen(headA)
        lb = self.getListLen(headB)
        if la < lb:
            la, lb = lb, la
            headA, headB = headB, headA
        while la>lb:
            headA = headA.next
            la -= 1
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next

        return headA


solu = Solution()
headA = solu.arrayToList(list(range(2)))
headB = ListNode(10)
# headB
print(solu.getIntersectionNode(headA, headB).val)
