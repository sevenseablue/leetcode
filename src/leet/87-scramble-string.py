
import collections
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        stack = []
        que = collections.deque(s2)
        for i in range(len(s1)):
            c = s1[i]
            stack.append(c)
            while stack and que and stack[-1] == que[0]:
                stack.pop()
                que.popleft()
        if not que and not stack:
            return True
        else:
            return False
class Solution:
    def isScramble(self, s1, s2):
        s1 = "banana"


solu = Solution()
s1 = "12345"
s2 = "31452"
print(solu.isScramble(s1, s2))


