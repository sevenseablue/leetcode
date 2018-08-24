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
        headold = head
        next = head.next
        while head and next:
            prev = head
            head = next
            next = head.next
            head.next = prev
            if prev == headold:
                prev.next = None

        return head

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


solu = Solution()
for i in range(5):
    head = solu.arrayToList(list(range(i)))
    head = solu.reverseList(head)
    print(solu.listToArray(head))
