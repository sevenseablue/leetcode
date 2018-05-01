# -*- coding: utf-8 -*-
"""
__author__ = 'wangdawei'
__time__ = '18-1-13 上午8:34'
"""
class Solution_dp:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                # print("(%s, %s) not in memo" % (i, j))
                if j == len(p):
                    ans = i == len(s)
                else:
                    # firstMatch = p[j] in {s[i], "?", "*"}
                    iIn = i < len(s)
                    if iIn and (p[j] == "?" or p[j] == s[i]):
                        ans = dp(i + 1, j + 1)
                    elif p[j] == "*":
                        ans = dp(i, j + 1) or (iIn and dp(i + 1, j)) or (iIn and dp(i + 1, j + 1))
                    else:
                        ans = False
                memo[(i, j)] = ans
            # print("memo[(%s, %s)]" % (i, j), memo[(i, j)])
            return memo[(i, j)]

        return dp(0, 0)
        pass

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        pi, si, last_si, lastpi = 0, 0, -1, -1
        while si < len(s):
            if pi < len(p) and (s[si] == p[pi] or p[pi] == '?'):
                si += 1
                pi += 1
            elif pi < len(p) and p[pi] == '*':
                pi += 1
                last_si = si
                lastpi = pi
            elif lastpi != -1:
                last_si += 1
                si = last_si
                pi = lastpi
            else:
                return False

        while pi < len(p) and p[pi] == '*':
            pi += 1

        return pi == len(p)


def main():
    solution = Solution()
    # solution.isMatch("aa", "a")
    # exit(-1)
    # solution.isMatch("aa", "aa")
    # solution.isMatch("aaa", "aa")
    # solution.isMatch("aa", "a*")
    # solution.isMatch("aa", ".*")
    # solution.isMatch("ab", ".*")
    # solution.isMatch("aab", "c*a*b")

    # assert (solution.isMatch("aa", "a") == False)
    # assert (solution.isMatch("aa", "aa") == True)
    # assert (solution.isMatch("aaa", "aa") == False)
    assert (solution.isMatch("", "*") == True)
    assert (solution.isMatch("", "*?") == False)
    assert (solution.isMatch("aa", "??") == True)
    assert (solution.isMatch("aa", "*") == True)

    assert (solution.isMatch("aa", "a*") == True)
    assert (solution.isMatch("ab", "?*") == True)
    assert (solution.isMatch("aab", "c*a*b") == False)

    exit()
    assert (solution.isMatch("a", "ab*a") == False)
    assert (solution.isMatch("ab", ".*..") == True)
    assert (solution.isMatch("aa", "a") == False)
    assert (solution.isMatch("aa", "aa") == True)
    assert (solution.isMatch("aaa", "aa") == False)
    assert (solution.isMatch("aa", "a*") == True)
    assert (solution.isMatch("", ".*") == True)
    assert (solution.isMatch("aa", ".*") == True)
    assert (solution.isMatch("ab", ".*") == True)
    assert (solution.isMatch("ab", ".*b.*") == True)
    assert (solution.isMatch("abab", ".*b.*") == True)
    assert (solution.isMatch("abab", ".*b.*b") == True)
    assert (solution.isMatch("abab", ".*ba*.*a*b") == True)
    assert (solution.isMatch("ababc", ".*ba*.*a*b") == False)
    assert (solution.isMatch("abab", ".*ba*.*a*") == True)
    assert (solution.isMatch("abab", ".*ba*.*a*c") == False)
    assert (solution.isMatch("abab", ".*ba*.*a*c.*") == False)
    assert (solution.isMatch("abab", ".*ba*.*a*b") == True)
    assert (solution.isMatch("", "a*a*a*") == True)
    assert (solution.isMatch("a", "a*a*a*") == True)
    assert (solution.isMatch("b", "a*b*a*") == True)
    assert (solution.isMatch("aab", "c*a*b") == True)
    assert (solution.isMatch("aab", "c*a*b") == True)
    assert (solution.isMatch("aab", "c*a*b") == True)


if __name__ == "__main__":
    main()
