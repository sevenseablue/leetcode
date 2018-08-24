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

import heapq

class Solution:

    def printLinkedList(self, head):
        while head:
            print(head.val)
            head = head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for i, listNode in enumerate(lists):
            if listNode:
                heapq.heappush(heap, (listNode.val, i, listNode))
        head, tail = None, None
        while heap:
            val, ind, node = heapq.heappop(heap)
            if not head:
                head = node
            else:
                tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, ind, node.next))

        return head

solu = Solution()
h1 = ListNode(0)
h1.next = ListNode(1)
h2 = ListNode(0)
h2.next = ListNode(1)
h3 = ListNode(1)
h3.next = ListNode(3)
h = solu.mergeKLists([h1, h2, None, h3])
solu.printLinkedList(h)

