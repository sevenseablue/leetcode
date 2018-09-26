import collections
class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.que = collections.deque(A)
        print(self.que)

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n>0 and self.que:
            topn = self.que[0]
            topv = self.que[1]

            if topn>n:
                self.que[0] -= n
                return topv
            elif topn == n:
                self.que.popleft()
                self.que.popleft()
                return topv
            else:
                self.que.popleft()
                self.que.popleft()
                n -= topn
        return -1


# Your RLEIterator object will be instantiated and called as such:
A = [3,8,0,9,2,5]
obj = RLEIterator(A)
for n in [2, 1, 1, 2]:
    param_1 = obj.next(n)
    print(param_1)