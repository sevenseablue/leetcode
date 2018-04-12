# coding: utf8
"""
---------------------------------------------
    File Name: bus_route
    Description: 
    Author: wangdawei
    date:   2018/4/11
---------------------------------------------
    Change Activity: 
                    2018/4/11
---------------------------------------------    
"""

class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        stationToRoute = {}
        for i in range(len(routes)):
            r = routes[i]
            for s in r:
                stationToRoute.setdefault(s, set([]))
                stationRoutes = stationToRoute.get(s)
                stationRoutes.add(i)

        cur_stations = [(S, 0)]
        stationLength = {}
        stationLength[S] = 0
        while len(cur_stations) > 0:
            s, cur_r = cur_stations.pop(0)
            # print("pop", s, cur_r)
            curRoutes = stationToRoute[s]
            for r in curRoutes:
                for s in routes[r]:
                    if s not in stationLength:
                        # print("put", s, cur_r+1)
                        stationLength[s] = cur_r + 1
                        cur_stations.append((s, cur_r + 1))

        if T in stationLength:
            return stationLength[T]
        else:
            return -1



solution = Solution()
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
print(solution.numBusesToDestination(routes, S, T))