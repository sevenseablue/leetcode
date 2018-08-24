# coding: utf8
"""
---------------------------------------------
    File Name: stairs
    Description: 
    Author: wangdawei
    date:   2018/5/7
---------------------------------------------
    Change Activity: 
                    2018/5/7
---------------------------------------------    
"""
class Solution:

    def __init__(self):
        self.__cache = {}
    def pathN(self, n):
        print("#" * 10, n)
        if n in self.__cache:
            return self.__cache[n]

        if n == 0:
            result = []
        elif n == 1:
            result = [[1]]
        elif n == 2:
            result = [[1, 1], [2]]
        elif n == 3:
            result = [[3], [2, 1], [1, 2], [1, 1, 1]]
        else:
            result = []
            for e in self.pathN(n-1):
                ec = e.copy()
                ec.append(1)
                print(ec)
                result.append(ec)
            for e in self.pathN(n-2):
                ec = e.copy()
                ec.append(2)
                result.append(ec)
            for e in self.pathN(n-3):
                ec = e.copy()
                ec.append(3)
                result.append(ec)

        self.__cache[n] = result
        return result

solu = Solution()
result = solu.pathN(5)
print(sorted(result))
print(len(result))
