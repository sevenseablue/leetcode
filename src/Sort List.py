__author__ = 'Administrator'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getLength(self, head):
        length = 0
        while head != None:
            length += 1
            head = head.next
        return length

    def swap(self, h, t):
        h.next = t.next
        t.next = h

    def mergeTwoList(self, h1, h2,):
        if h1.val > h2.val:
            head = h2
        else:
            head = h1

        while h1 != None and h2 != None:
            if h1.val > h2.val:
                small = h2
                large = h1
            else:
                small = h1
                large = h2
            while small.next != None and small.next.val <= large.val:
                small = small.next
            small.next = large
            h1 = small.next
            h2 = large

        return head

    def mergeSort(self, head, length, step):
        curHead = head
        h = curHead
        t = curHead.next
        if h.val > t.val:
            self.swap(h, t)


    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        length = self.getLength(head)
        step = 2

solu = Solution()

for i in range(1, 4, 1):
    print i
    head = ListNode(i)
    cur = head
    for j in range(1,i):
        cur.next = ListNode(j)
        cur = cur.next

    print solu.getLength(head)



