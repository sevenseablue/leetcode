# coding: utf8
"""
---------------------------------------------
    File Name: heap_t
    Description: 
    Author: wangdawei
    date:   2018/1/26
---------------------------------------------
    Change Activity: 
                    2018/1/26
---------------------------------------------    
"""

import heapq
import random

heap = list(range(10))
# heapq._heapify_max(heap)
print(heap)
for i in range(10):
    heapq._heapify_max(heap)
    print(heapq.heappop(heap))

print(heap)


exit()
for i in range(15):
    item = random.randint(10, 100)
    print("comeing ", item, )
    if len(heap) >= 5:
        top_item = heap[0]  # smallest in heap
        if top_item < item:  # min heap
            top_item = heapq.heappop(heap)
            print("pop", top_item, )
            heapq.heappush(heap, item)
            print("push", item, )
            print(heap[0])
    else:
        heapq.heappush(heap, item)
        print("push", item, )
        print(heap[0])
    pass
    print(heap)
pass
print(heap)


print("sort")
heap.sort()

print(heap)
