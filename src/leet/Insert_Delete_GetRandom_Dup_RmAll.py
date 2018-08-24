# coding: utf8
"""
---------------------------------------------
    File Name: LRU Cache
    Description: 
    Author: wangdawei
    date:   2018/1/16
---------------------------------------------
    Change Activity: 
                    2018/1/16
---------------------------------------------    
"""

import random


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals, self.dic = [], {}


    def insert(self, val):
        """
        Inserts a value to the set.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            self.dic[val].add(len(self.vals))
            self.vals.append(val)
            return False
        else:
            self.dic[val] = set([len(self.vals)])
            self.vals.append(val)
            return True



    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            posSet = self.dic[val].copy()
            for pos in sorted(list(posSet), reverse=True):
                toRemoveIdx = len(self.vals) - 1
                self.vals[pos] = self.vals[toRemoveIdx]
                toSwap = self.dic[self.vals[pos]]
                toSwap.remove(toRemoveIdx)
                toSwap.add(pos)
                self.vals.pop()
                # self.dic[val].remove(pos)
            self.dic.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.vals) > 0:
            idx = random.randint(0, len(self.vals) - 1)
            return self.vals[idx]
        else:
            return None



def main():
    randomSet = RandomizedCollection()

    print(randomSet.insert(1))
    print(randomSet.insert(1))
    # print(randomSet.insert(1))
    # print(randomSet.getRandom())
    print(randomSet.remove(1))
    # print(randomSet.insert(2))
    print(randomSet.getRandom())
    pass


if __name__ == "__main__":
    main()