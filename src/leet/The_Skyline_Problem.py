# coding: utf8
"""
---------------------------------------------
    File Name: The_Skyline_Problem
    Description: 
    Author: wangdawei
    date:   2018/1/23
---------------------------------------------
    Change Activity: 
                    2018/1/23
---------------------------------------------    
"""


#
# https://briangordon.github.io/2014/08/the-skyline-problem.html

class MaxHeap:
    # self defined elements
    # self defined compare function for sort
    # self defined, get max element, not only pop max element, o(1)
    # self defined, delete any element, not only the max element, o(log(n))
    def __init__(self, buildings):
        self.buildings = buildings
        self.size = 0
        self.heap = [None] * (2 * len(buildings) + 1)
        self.lineMap = dict()
    def maxLine(self):
        return self.heap[1]
    def insert(self, lineId):
        self.size += 1
        self.heap[self.size] = lineId
        self.lineMap[lineId] = self.size
        self.siftUp(self.size)
    def delete(self, lineId):
        heapIdx = self.lineMap[lineId]
        self.heap[heapIdx] = self.heap[self.size]
        self.lineMap[self.heap[heapIdx]] = heapIdx
        self.heap[self.size] = None
        del self.lineMap[lineId]
        self.size -= 1
        # it is ok to add if heapIdx != self.size + 1:
        self.siftUp(heapIdx)   # added by wangdawei
        self.siftDown(heapIdx)
    def siftUp(self, idx):
        # idx <= self.size added by wangdawei
        while 1 < idx <= self.size and self.cmp(idx // 2, idx) < 0:
            self.swap(idx // 2, idx)
            idx //= 2
    def siftDown(self, idx):
        while idx * 2 <= self.size:
            nidx = idx * 2
            if idx * 2 + 1 <= self.size and self.cmp(idx * 2 + 1, idx * 2) > 0:
                nidx = idx * 2 + 1
            if self.cmp(nidx, idx) > 0:
                self.swap(nidx, idx)
                idx = nidx
            else:
                break
    def swap(self, a, b):
        la, lb = self.heap[a], self.heap[b]
        self.lineMap[la], self.lineMap[lb] = self.lineMap[lb], self.lineMap[la]
        self.heap[a], self.heap[b] = lb, la
    def cmp(self, a, b):
        return self.buildings[self.heap[a]][2] - self.buildings[self.heap[b]][2]

class Solution:
    def getSkyline(self, buildings):
        size = len(buildings)
        points = sorted([(buildings[x][0], x, 's') for x in range(size)] +
                        [(buildings[x][1], x, 'e') for x in range(size)])
        maxHeap = MaxHeap(buildings)
        ans = []
        for p in points:
            if p[2] == 's':
                maxHeap.insert(p[1])
            else:
                maxHeap.delete(p[1])
            maxLine = maxHeap.maxLine()
            height = buildings[maxLine][2] if maxLine is not None else 0
            # the first。 上一个点的坐标等于这个点的坐标， 重合了
            if len(ans) == 0 or ans[-1][0] != p[0]:
                ans.append([p[0], height])
            # 不重合， 一个矩形的开始
            elif p[2] == 's':
                ans[-1][1] = max(ans[-1][1], height)
            # 不重合， 一个矩形的结束
            else:
                ans[-1][1] = min(ans[-1][1], height)
            # 不同坐标的点， 相同的高度， pop the last one
            if len(ans) > 1 and ans[-1][1] == ans[-2][1]:
                ans.pop()
        return ans

solu = Solution()

l1 = [ [2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8] ]
print(solu.getSkyline(l1))
l2 = [ [2,10], [3,15], [7,12], [12,0], [15,10], [20,8], [24, 0] ]

