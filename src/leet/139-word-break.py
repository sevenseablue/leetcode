class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        cache = {"": True}
        def wordSeg(s1):
            if s1 in cache:
                # print("in", s1)
                return cache[s1]

            for i in range(1, len(s1)+1):
                if s1[:i] in wordDict:
                    if wordSeg(s1[i:]):
                        cache[s1] = True
                        # print("True", s1)
                        return True
            cache[s1] = False
            # print("False", s1)
            return False

        return wordSeg(s)

solu = Solution()
s = "applepenapple"
wordDict = ["apple", "pen"]
print(solu.wordBreak(s, wordDict))

s = "catsandog"
wordDict = ["cat", "cats", "dog", "sand", "and", "cat", "og"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# s = "leetcode"
# wordDict = ["leet","code"]
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
print(solu.wordBreak(s, wordDict))
