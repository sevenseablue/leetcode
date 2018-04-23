# coding: utf8
"""
---------------------------------------------
    File Name: 5-longest-palindromic-substring
    Description: 
    Author: wangdawei
    date:   2018/4/23
---------------------------------------------
    Change Activity: 
                    2018/4/23
---------------------------------------------    
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        maxLen = 1
        start = 0

        for i in range(len(s)):
            if i + 1 - maxLen >= 2 and s[i - maxLen - 1: i + 1] == s[i - maxLen - 1: i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue
            if i + 1 - maxLen >= 1 and s[i - maxLen: i + 1] == s[i - maxLen: i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
            pass
        return s[start:start+maxLen]

solu = Solution()
for i in range(6):
    s = "a" * i
    print(s, solu.longestPalindrome(s))
