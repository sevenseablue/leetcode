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


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals, self.dic = [], {}


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.vals:
            self.vals.append(val)
            self.dic[val] = len(self.vals) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            pos = self.dic[val]
            self.vals[pos] = self.vals[-1]
            self.dic[self.vals[-1]] = pos
            self.vals.pop()
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
    randomSet = RandomizedSet()

    print(randomSet.insert(1))
    print(randomSet.remove(2))
    print(randomSet.insert(2))
    print(randomSet.getRandom())
    print(randomSet.remove(1))
    print(randomSet.insert(2))
    print(randomSet.getRandom())
    pass


if __name__ == "__main__":
    main()