# coding: utf8
"""
---------------------------------------------
    File Name: 2-add-two-numbers
    Description: 
    Author: wangdawei
    date:   2018/4/20
---------------------------------------------
    Change Activity: 
                    2018/4/20
---------------------------------------------    
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1, l2
        res = ListNode(0)
        cur = res
        ten, n1, n2 = 0, 0, 0
        while l1 is not None or l2 is not None or ten != 0:
            if l1 is None:
                n1 = 0
            else:
                n1 = l1.val
                l1 = l1.next
            if l2 is None:
                n2 = 0
            else:
                n2 = l2.val
                l2 = l2.next

            num = n1 + n2 + ten
            one = num % 10
            ten = num // 10
            # print("one", one)
            cur.next = ListNode(one)
            cur = cur.next

        res = res.next
        return res


solu = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(8)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
res = solu.addTwoNumbers(l1, l2)
while res is not None:
    print(res.val)
    res=res.next
