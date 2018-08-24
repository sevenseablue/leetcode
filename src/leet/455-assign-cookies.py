
import bisect
class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        ss = sorted(s)
        result = 0
        for g1 in g:
            ind = bisect.bisect_left(ss, g1)
            if ind < len(ss):
                result += 1
                ss.pop(ind)

        return result



solu = Solution()
g, s = [1,2], [1,2,3]
print(solu.findContentChildren(g, s))
g, s = [1,2,3], [1,1]
g, s = [10,9,8,7], [5,6,7,8]
print(solu.findContentChildren(g, s))