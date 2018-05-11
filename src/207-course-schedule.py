# coding: utf8
"""
---------------------------------------------
    File Name: 207-course-schedule
    Description: 
    Author: wangdawei
    date:   2018/5/7
---------------------------------------------
    Change Activity: 
                    2018/5/7
---------------------------------------------    
"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        s2e = {}
        e2s = {}
        for s, e in prerequisites:
            s2e[s] = s2e.get(s, [])
            s2e[s].append(e)
            e2s[e] = e2s.get(e, [])
            e2s[e].append(s)

        delNodes = set([])
        while True:
            thisNum = 0
            for i in range(numCourses):
                # print("ing", i)
                if i in delNodes:
                    # print("deleted", i)
                    continue
                if i not in e2s or len(e2s[i]) == 0:
                    # print("deleting", i)
                    delNodes.add(i)
                    thisNum += 1
                    if i in s2e:
                        for j in s2e[i]:
                            e2s[j].remove(i)
                        s2e[i] = []
            if thisNum == 0 or len(delNodes) == numCourses:
                break
        # print(delNodes, thisNum)
        return len(delNodes) == numCourses

solu = Solution()
print(solu.canFinish(2, [[1,0]] ))
print(solu.canFinish(2, [[1,0],[0,1]]))
