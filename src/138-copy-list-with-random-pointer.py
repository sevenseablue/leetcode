#!/home/wangdawei/anaconda2/envs/py3/bin/python 
# -*- coding: utf-8 -*-  
""" 
 @desc: 
 @author: wangdawei 
 @contact: 178129482@qq.com  
"""  
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def printLinkedList(self, head):
        while head:
            print(head.label, head.next.label if head.next else None, head.random.label if head.random else None)
            head = head.next

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        headOld = head
        d = {}
        while head:
            # print(head.label)
            d[head] = RandomListNode(head.label)
            head = head.next
        head = headOld
        while head:
            # print(head.label)
            if head.next:
                d[head].next = d[head.next]
            if head.random:
                d[head].random = d[head.random]
            head = head.next

        return d[headOld]

solu = Solution()
head = RandomListNode(0)
# head.next = RandomListNode(1)
# head.next.next = RandomListNode(2)
# head.random = head.next
# head.next.random = head
solu.printLinkedList(head)
headcp = solu.copyRandomList(head)
solu.printLinkedList(headcp)

