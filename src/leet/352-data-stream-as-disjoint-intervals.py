# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return "[%s,%s]" % (self.start, self.end)
from blist import sorteddict
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # all ints map to the interval left
        self.left = {}
        # current intervals left to current intervals, pop and add
        self.intervals = sorteddict()
        # self.intervals = {}


    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.left:
            return

        if val + 1 in self.left:
            if val - 1 in self.left:
                leftmost = self.left[val - 1]
            else:
                leftmost = val
            self.left[val] = leftmost
            interval = self.intervals[val + 1]
            self.left[interval.start] = leftmost
            self.left[interval.end] = leftmost

            self.intervals[leftmost] = Interval(leftmost, interval.end)
            self.intervals.pop(val + 1)
        elif val - 1 in self.left:
            self.left[val] = self.left[val - 1]
            self.intervals[self.left[val]].end = val
        else:
            self.left[val] = val
            self.intervals[val] = Interval(val, val)


    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals.values()
        # return [self.intervals[e] for e in sorted(self.intervals.keys())]
        # return sorted(list(self.intervals.values()), key=lambda x: x.start)



from bisect import bisect


class SummaryRangesB(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.inter = [], []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        i = bisect(self.nums, val)
        if i == 0:
            if i < len(self.nums) and val == self.nums[i] - 1:
                self.nums[i] -= 1
                self.inter[i].start -= 1
            else:
                self.nums.insert(i, val)
                self.inter.insert(i, Interval(val, val))
        elif val > self.inter[i - 1].end:
            if val == self.inter[i - 1].end + 1:
                self.inter[i - 1].end += 1
                if i < len(self.nums) and self.nums[i] - self.inter[i - 1].end == 1:
                    self.inter[i - 1].end = self.inter[i].end
                    self.nums.pop(i)
                    self.inter.pop(i)
            elif i < len(self.nums) and val == self.nums[i] - 1:
                self.nums[i] -= 1
                self.inter[i].start -= 1
            else:
                self.nums.insert(i, val)
                self.inter.insert(i, Interval(val, val))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.inter

# Your SummaryRanges object will be instantiated and called as such:

import time
nums = list(range(100000, 0, -2))
t1 = time.time()
obj = SummaryRanges()
# for val in [1, 3, 7, 2, 6]:
for val in nums:
    obj.addNum(val)
    param_2 = obj.getIntervals()
    # print(param_2)
print(time.time() - t1)
t1 = time.time()
obj = SummaryRangesB()
# for val in [1, 3, 7, 2, 6]:
for val in nums:
    obj.addNum(val)
    param_2 = obj.getIntervals()
    # print(param_2)
print(time.time() - t1)
t1 = time.time()