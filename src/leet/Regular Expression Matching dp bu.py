# coding: utf8
"""
---------------------------------------------
    File Name: Regular Expression Matching dp bu
    Description: 
    Author: wangdawei
    date:   2018/1/11
---------------------------------------------
    Change Activity: 
                    2018/1/11
---------------------------------------------    
"""

class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]

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