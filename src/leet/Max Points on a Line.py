__author__ = 'Administrator'

#Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

# N^2
class Solution:
    def angle(self, p1, p2):
        if p1.x == p2.x:
            return float("Inf")
        else:
            return (p2.y-p1.y)*1.0/(p2.x-p1.x)

    def isSamePoint(self, p1, p2):
        if p1.x == p2.x and p1.y == p2.y:
            return True
        else:
            return False

    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        Max = 2
        for p1 in points:
            d = {}
            samePointCount = 0
            for p2 in points:
                if self.isSamePoint(p1, p2):
                    samePointCount += 1
                    continue
                angleTmp = self.angle(p1, p2)
                angleCount = d.get(angleTmp, 0)
                d[angleTmp] = angleCount + 1
            if Max < samePointCount:
                Max = samePointCount
            for v in list(d.values()):
                if v+samePointCount > Max:
                    Max = v+samePointCount
        return Max

# N^3
class SolutionN3:
    def inALine(self, p1, p2, p3):
        if p1.x == p2.x and p2.x == p3.x:
            return True
        elif p1.x == p2.x or p2.x == p3.x:
            return False
        elif (p2.y-p1.y)*1.0/(p2.x-p1.x) == (p3.y-p2.y)*1.0/(p3.x-p2.x):
            return True
        else: return False
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        maxNum = 2
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                curMax = 2
                for k in range(j+1, len(points)):
                    if  self.inALine(points[i], points[j], points[k]):
                        curMax = curMax + 1
                if maxNum < curMax:
                    maxNum = curMax

        return maxNum


points = []
for i in range(5):
    for j in range(5):
        points.append(Point(i, j))
        points.append(Point(i, j))
points.append(Point(0, 5))
points.append(Point(0, 5))
points.append(Point(0, 5))

#points = [(1,1),(1,1),(1,1),(1,1)]
#points = [(1,1),(1,1),(2,2),(2,2)]

solu = SolutionN3()
print(solu.maxPoints(points))

solu = Solution()
print(solu.maxPoints(points))

