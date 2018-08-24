# coding: utf8
"""
---------------------------------------------
    File Name: Word Break II
    Description: 
    Author: wangdawei
    date:   2018/1/16
---------------------------------------------
    Change Activity: 
                    2018/1/16
---------------------------------------------    
"""


class Solution:
    def __init__(self):
        self.d = {}

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ls = len(s)
        result = []
        for i in range(ls):
            s1 = s[0: i+1]
            if s1 in wordDict:
                if i + 1 < ls:
                    s2 = s[i+1:]
                    if s2 in self.d:
                        tmp_strs = self.d[s2]
                    else:
                        tmp_strs = self.wordBreak(s2, wordDict)
                        self.d[s2] = tmp_strs
                    if len(tmp_strs) > 0:
                        result.extend([s1 + " " + e for e in tmp_strs])
                        pass
                elif i+1 == ls:
                    result.append(s1)
                    pass
        print("#", ls,  len(self.d))
        return result


def main():
    s = "catsanddog"
    # s = "dog"
    s = "aaaaa"
    dict = ["cat", "cats", "and", "sand", "dog", "a", "aa"]
    ["cats and dog", "cat sand dog"]

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    s = "a" * 23
    dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa",]
    solu = Solution()
    print(len(s))
    solu.wordBreak(s, dict)
    # print(solu.wordBreak(s, dict))

if __name__ == "__main__":
    main()