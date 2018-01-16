# coding: utf8
"""
---------------------------------------------
    File Name: Minimum Window Substring
    Description: 
    Author: wangdawei
    date:   2018/1/15
---------------------------------------------
    Change Activity: 
                    2018/1/15
---------------------------------------------    
"""


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        d = {}
        for e in t:
            if e in d:
                d[e] += 1
            else:
                d[e] = 1

        i, j, ls, lt, lti = 0, 0, len(s), len(t), len(t)
        l, r = 0, 0
        minl = ls + 1
        minw = ""
        while i < ls:
            e = s[i]
            if e in d:
                if d[e] > 0:
                    lti -= 1
                d[e] -= 1
                if lti == 0:
                    while j <= i:
                        ej = s[j]
                        if ej not in d:
                            j += 1
                        elif d[ej] < 0:
                            d[ej] += 1
                            j += 1
                        else:
                            if i + 1 - j < minl:
                                minl = i + 1 - j
                                minw = s[j:i + 1]
                            break
                i += 1
            else:
                i += 1

        return minw

        pass


def main():
    solu = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(solu.minWindow(s, t))
    print(solu.minWindow("", ""))
    print(solu.minWindow("", "a"))
    print(solu.minWindow("a", ""))
    print(solu.minWindow("a", "a"))
    print(solu.minWindow("aaa", "aa"))
    print(solu.minWindow("abbbac", "abc"))
    print(solu.minWindow("abbbcabbbac", "abc"))
    print(solu.minWindow("aaa", "aa"))
    print(solu.minWindow("cabwefgewcwaefgcf", "cae"))
    print(solu.minWindow("b", "a"))
    print(solu.minWindow("a", "b"))


if __name__ == "__main__":
    main()
