# coding: utf8
"""
---------------------------------------------
    File Name: Merge k Sorted Lists
    Description: 
    Author: wangdawei
    date:   2018/2/8
---------------------------------------------
    Change Activity: 
                    2018/2/8
---------------------------------------------    
"""

import heapq
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __eq__(self, other):
    #     return self.val == other.val
    #
    # def __lt__(self, other):
    #     return self.val < other.val
    #
    # def __repr__(self):
    #     if self:
    #         return str(self.val)

class CmpListNode:
    def __init__(self, node):
        self.node = node

    def __eq__(self, other):
        return self.node.val == other.node.val

    def __lt__(self, other):
        return self.node.val < other.node.val

    def __repr__(self):
        if self:
            return str(self.node.val)

class Solution:

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for l in lists:
            if l:
                heap.append(CmpListNode(l))
        heapq.heapify(heap)
        head = None
        tail = None
        while len(heap)>0:
            node = heapq.heappop(heap).node
            if head is None:
                head = node
            if tail is None:
                tail = node
            else:
                tail.next = node
                tail = tail.next
            if node.next:
                heapq.heappush(heap, CmpListNode(node.next))

        return head

def travel(head):
    cur = head
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

def main():
    lists = []
    for i in range(10):
        head = None
        cur = None
        for j in range(10):
            # i1 = random.randint(0, 100)
            node = ListNode(j)
            if head is None:
                head = node
            if cur is None:
                cur = node
            else:
                cur.next = node
                cur = cur.next
        lists.append(head)
    # for l in lists:
    #     travel(l)
    # lists = []
    solu = Solution()
    head = solu.mergeKLists(lists)
    # print(head)
    travel(head)

if __name__ == "__main__":
    main()





