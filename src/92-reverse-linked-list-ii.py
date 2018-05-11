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

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        firstHead = head
        i = 1
        newhead = None
        firstTail = None
        while i<=n:
            if i < m:
                firstTail = head
                head = head.next
            if i>=m and i<=n:
                next = head.next
                head.next = newhead
                newhead = head
                head = next
                if i == m:
                    midtail = newhead
                if i == n:
                    midhead = newhead
                    thirdHead = head
            i += 1

        if m > 1:
            firstTail.next = midhead
            midtail.next = thirdHead
            return firstHead
        else:
            midtail.next = thirdHead
            return midhead

solu = Solution()
for i in range(4, 5):
    head = solu.arrayToList(list(range(i)))
    head = solu.reverseBetween(head, 2, 3)
    print(solu.listToArray(head))
