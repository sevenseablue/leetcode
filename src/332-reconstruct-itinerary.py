# coding: utf8
"""
---------------------------------------------
    File Name: 332-reconstruct-itinerary
    Description: 
    Author: wangdawei
    date:   2018/5/8
---------------------------------------------
    Change Activity: 
                    2018/5/8
---------------------------------------------    
"""


import bisect, collections
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = {}
        for v1, v2 in tickets:
            graph[v1] = graph.get(v1, [])
            bisect.insort(graph[v1], v2)
            print(v1, graph[v1])

        s="JFK"
        result = []
        result.append(s)
        index = {}
        for k in graph.keys():
            index[k] = 0
        while s in index and index[s] < len(graph[s]):
            e=graph[s][index[s]]
            index[s] += 1
            result.append(e)
            s=e

        return result

    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        for k, v in targets.items():
            print(k, v)
        route = []
        def visit(airport):
            while targets[airport]:
                print(targets[airport])
                visit(targets[airport].pop())
            route.append(airport)
            print("route,", route)
        visit('JFK')
        return route[::-1]

solu = Solution()
for tickets in [[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]], [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]]:
    print(solu.findItinerary(tickets))
