# -*- coding: utf-8 -*-
"""
__author__ = 'wangdawei'
__time__ = '18-5-1 下午11:35'
"""
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodesDict = {}
        for n1, n2 in edges:
            nodesDict[n1] = nodesDict.get(n1, set([]))
            nodesDict.get(n1).add(n2)
            nodesDict[n2] = nodesDict.get(n2, set([]))
            nodesDict.get(n2).add(n1)


        while True:
            popList = []
            for n1, n2s in nodesDict.items():
                if len(n2s) == 1:
                    popList.append(n1)
            # print(popList)
            if popList:
                for n1 in popList:
                    # print(n1)
                    n2set = nodesDict.get(n1)
                    if n2set:
                        n2 = n2set.pop()
                    nodesDict.pop(n1)
                    n1set = nodesDict.get(n2)
                    if n1set:
                        n1set.remove(n1)
                pass
            else:
                break
        result = []
        if nodesDict:
            # print("cycles")
            for n1, n2 in edges:
                if n1 in nodesDict and n2 in nodesDict:
                    result = [n1, n2]
        return result


solu = Solution()
for l1 in [[[1,2], [1,3], [2,3]], [[1,2], [2,3], [3,4], [1,4], [1,5]],
           [[1, 2]]]:
    print(solu.findRedundantConnection(l1))

