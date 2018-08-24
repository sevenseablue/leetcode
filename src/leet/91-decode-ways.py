#!/home/wangdawei/anaconda2/envs/py3/bin/python
# -*- coding: utf-8 -*-  
""" 
 @desc: 
 @author: wangdawei 
 @contact: 178129482@qq.com  
"""


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # code = [""]*26
        # for i in range(65, 91):
        #     code[i-65] = chr(i)
        if len(s) == 0:
            return 1

        dp = [0]*(len(s) + 1)
        dp[0] = 1
        for i in range(0, len(s)):
            if i==0 and s[i] == "0":
                return 0
            if s[i] == "0" and s[i-1] not in {"1", "2"}:
                return 0
            if i == 0:
                dp[i+1] = 1
            elif s[i] == "0" and s[i - 1] in {"1", "2"}:
                dp[i+1] = dp[i-1]
            else:
                if s[i-1] == "0":
                    dp[i+1] = dp[i]
                else:
                    dp[i+1] = dp[i] + (dp[i-1] if 1 <= int(s[i-1:i+1]) <= 26 else 0)
        # print(dp)
        return dp[-1]

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # code = [""]*26
        # for i in range(65, 91):
        #     code[i-65] = chr(i)
        # if len(s) == 0:
        #     return 1
        # if len(s) == 0:
        #     return 1

        dp = [0]*(len(s) + 1)
        dp[0] = 1
        for i in range(0, len(s)):
            if i==0 and s[i] == "0":
                return 0
            if s[i] == "0" and s[i-1] not in {"1", "2"}:
                return 0

            # dp[i+1] = (0 if i > 0 and s[i-1:i+1] in {"10", "20"} else dp[i]) + (dp[i-1] if i > 0 and 10 <= int(s[i-1:i+1]) <= 26 else 0)
            if s[i] == "0" and s[i - 1] in {"1", "2"}:
                dp[i+1] = dp[i-1]
            else:
                dp[i+1] = dp[i] + (dp[i-1] if i > 0 and 10 <= int(s[i-1:i+1]) <= 26 else 0)
        # print(dp)
        return dp[-1]

solu = Solution()
for s in ["12", "226", "", "1", "27", "99", "100", "227", "230", "231023", "231003", "110"]:
    # print(s)
    print (solu.numDecodings(s))

