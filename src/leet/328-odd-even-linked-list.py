#!/home/wangdawei/anaconda2/envs/py3/bin/python 
# -*- coding: utf-8 -*-  
""" 
 @desc: 
 @author: wangdawei 
 @contact: 178129482@qq.com  
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        newhead = None
        while head:
            next = head.next
            head.next = newhead
            newhead = head
            head = next

        return newhead

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        i = 3
        oddh = head
        evenh = head.next
        curo = oddh
        cure = evenh
        head = head.next.next
        while head:
            if i % 2 == 1:
                curo.next = head
                curo = curo.next
            elif i % 2 == 0:
                cure.next = head
                cure = cure.next
            i += 1
            head = head.next
        curo.next = evenh
        cure.next = None

        return oddh


solu = Solution()
for i in range(0, 6):
    head = solu.arrayToList(list(range(i)))
    head = solu.oddEvenList(head)
    print(solu.listToArray(head))
