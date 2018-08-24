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

    def eleAppend(self, fh, ft, head):
        if not fh:
            fh = head
        else:
            ft.next = head
        ft = head


    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        fh, ft, sh, st = [None] * 4

        while head:
            if head.val < x :
                if not fh:
                    fh = head
                else:
                    ft.next = head
                ft = head
            else:
                if not sh:
                    sh = head
                else:
                    st.next = head
                st = head

            head = head.next

        if fh:
            ft.next = sh
            if st:
                st.next = None
            return fh
        return sh

solu = Solution()
head = solu.arrayToList(list(range(5, 0, -1)))
h = solu.partition(head, 3)
print(solu.listToArray(h))


