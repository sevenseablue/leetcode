# coding: utf8
"""
---------------------------------------------
    File Name: Find Median from Data Stream
    Description: 
    Author: wangdawei
    date:   2018/1/26
---------------------------------------------
    Change Activity: 
                    2018/1/26
---------------------------------------------    
"""

#
#
# class MaxHeap:
#     # self defined elements
#     # self defined compare function for sort
#     # self defined, get max element, not only pop max element, o(1)
#     # self defined, delete any element, not only the max element, o(log(n))
#     def __init__(self, buildings=[],  comp=lambda x,y: x-y):
#         self.objects = {}
#         self.size = 0
#         self.heap = [None] * (2 * 0 if buildings is None else len(buildings) + 1)
#         self.capacity = len(self.heap)
#         self.lineMap = dict()
#         self.comp = comp
#         self.topInd = 0
#         for b in buildings:
#             self.insert(b)
#
#     def insert(self, obj):
#         self.objects[self.topInd] = obj
#         self.insertLineId(self.topInd)
#         self.topInd += 1
#
#     def topLine(self):
#         if self.size<1:
#             return None
#         return self.objects[self.heap[1]]
#     def pop(self):
#         if self.size<1:
#             raise "error"
#         res = self.heap[1]
#         result = self.objects[res]
#         self.delete(res)
#         return result
#     def insertLineId(self, lineId):
#         # print("##", self.size, self.capacity)
#         if self.size + 1 >= self.capacity * 0.91:
#             tmp = [None] * (self.capacity + 1)
#             # print("capacity", self.capacity)
#             self.heap.extend(tmp)
#             self.capacity = len(self.heap)
#             # print("capacity", self.capacity)
#         self.size += 1
#         self.heap[self.size] = lineId
#         self.lineMap[lineId] = self.size
#         self.siftUp(self.size)
#     def delete(self, lineId):
#         heapIdx = self.lineMap[lineId]
#         heapIdxToDel = self.heap[heapIdx]
#         self.heap[heapIdx] = self.heap[self.size]
#         self.lineMap[self.heap[heapIdx]] = heapIdx
#         self.heap[self.size] = None
#         del self.lineMap[lineId]
#         self.size -= 1
#         # it is ok to add if heapIdx != self.size + 1:
#         self.siftUp(heapIdx)   # added by wangdawei
#         self.siftDown(heapIdx)
#         del self.objects[heapIdxToDel]
#     def siftUp(self, idx):
#         # idx <= self.size added by wangdawei
#         while 1 < idx <= self.size and self.cmp(idx // 2, idx) < 0:
#             self.swap(idx // 2, idx)
#             idx //= 2
#     def siftDown(self, idx):
#         while idx * 2 <= self.size:
#             nidx = idx * 2
#             if idx * 2 + 1 <= self.size and self.cmp(idx * 2 + 1, idx * 2) > 0:
#                 nidx = idx * 2 + 1
#             if self.cmp(nidx, idx) > 0:
#                 self.swap(nidx, idx)
#                 idx = nidx
#             else:
#                 break
#     def swap(self, a, b):
#         la, lb = self.heap[a], self.heap[b]
#         self.lineMap[la], self.lineMap[lb] = self.lineMap[lb], self.lineMap[la]
#         self.heap[a], self.heap[b] = lb, la
#     def cmp(self, a, b):
#         return self.comp(self.objects[self.heap[a]], self.objects[self.heap[b]])
#
#
# # maxheap = MaxHeap()
# # print(maxheap.topLine())
# # for i in range(0, 30):
# #     maxheap.insert(i)
# # minheap = MaxHeap(list(range(30, 40)), lambda x, y: y - x)
# # for i in range(20, 50):
# #     minheap.insert(i)
# #
# # print(maxheap.objects)
# # for i in range(5):
# #     print(maxheap.pop())
# # for i in range(5):
# #     print(minheap.pop())
#
#
# class MedianFinder:
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.maxheap = MaxHeap()
#         self.minheap = MaxHeap(comp=lambda x,y:y-x)
#
#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: void
#         """
#         if self.maxheap.size == 0:
#             self.maxheap.insert(num)
#         elif self.minheap.size == 0:
#             num1 = self.maxheap.pop()
#             num1, num2 = (num1, num) if num1 <= num else (num, num1)
#             self.maxheap.insert(num1)
#             self.minheap.insert(num2)
#         else:
#             num1 = self.maxheap.pop()
#             num2 = self.minheap.pop()
#             num1, mid, num2 = sorted([num1, num, num2])
#             self.maxheap.insert(num1)
#             self.minheap.insert(num2)
#             if self.maxheap.size <= self.minheap.size:
#                 self.maxheap.insert(mid)
#             else:
#                 self.minheap.insert(mid)
#
#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         if self.maxheap.size == 0:
#             return None
#         elif self.minheap.size == 0:
#             num1 = self.maxheap.topLine()
#             return num1
#         else:
#             num1 = self.maxheap.topLine()
#             num2 = self.minheap.topLine()
#             if self.maxheap.size == self.minheap.size:
#                 return (num1 + num2) / 2
#             elif self.maxheap.size == self.minheap.size + 1:
#                 return num1
#             elif self.maxheap.size == self.minheap.size - 1:
#                 return num2
#             else:
#                 raise "error"

from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__max_heap = []
        self.__min_heap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # Balance smaller half and larger half.
        if not self.__max_heap or num > -self.__max_heap[0]:
            heappush(self.__min_heap, num)
            if len(self.__min_heap) > len(self.__max_heap) + 1:
                heappush(self.__max_heap, -heappop(self.__min_heap))
        else:
            heappush(self.__max_heap, -num)
            if len(self.__max_heap) > len(self.__min_heap):
                heappush(self.__min_heap, -heappop(self.__max_heap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        return (-self.__max_heap[0] + self.__min_heap[0]) / 2.0 \
            if len(self.__min_heap) == len(self.__max_heap) \
            else self.__min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
for num in range(2, 10, 2):
    obj.addNum(num)
    param_2 = obj.findMedian()
    print(num, param_2)





