# coding: utf8
"""
---------------------------------------------
    File Name: LRU Cache
    Description: 
    Author: wangdawei
    date:   2018/1/16
---------------------------------------------
    Change Activity: 
                    2018/1/16
---------------------------------------------    
"""

class ListNode():
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        node.prev, node.next = None, None  # avoid dirty node
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self,node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.next, node.prev = None, None

        pass

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.list = LinkedList()
        self.dict = {}
        self.capacity = capacity

    def _insert(self, k, v):
        node = ListNode(k, v)
        self.dict[k] = node
        self.list.insert(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.list.delete(self.dict[key])
            self.list.insert(self.dict[key])
            return self.dict[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.list.delete(self.dict[key])
        elif len(self.dict) == self.capacity:
            del self.dict[self.list.head.key]
            self.list.delete(self.list.head)

        self._insert(key, value)


def main():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1)) # returns
    cache.put(3, 3)  # evicts
    cache.get(2) # returns - 1(not found)
    cache.put(4, 4) # evicts
    cache.get(1) # returns - 1(not found)
    cache.get(3) # returns
    cache.get(4) # returns
    pass


if __name__ == "__main__":
    main()