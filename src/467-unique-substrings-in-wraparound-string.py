class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        def ispsub(pstr):
            for s1,s2 in zip(pstr[:-1],pstr[1:]):
                if ord(s2)-ord(s1) != 1 and ord(s2)-ord(s1) != -25:
                    return False
            return True

        def lenpseq(pstr):
            d={}
            if pstr is None:
                return 0
            if len(pstr) <= 1:
                return len(pstr)
            count = 1
            maxcount = 1
            for s1,s2 in zip(pstr[:-1],pstr[1:]):
                if ord(s2)-ord(s1) != 1 and ord(s2)-ord(s1) != -25:
                    if count>= d.get(s2, 0):
                        d[s2] = count
                    count = 1
                else:
                    count += 1
                if count > maxcount:
                    maxcount = count
            return maxcount

        for s in p:
            pass

        for pstr in ["", "a", "ab", "za", "zab", "zabcdefghijklmnopqrstuvwxyzabc"]:
            print(ispsub(pstr))

        for i in range(1, len(p)+1):
            for j in range(0, len(p) - i + 1):
                pass

class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        cumu = 0
        d = {}
        for i in range(len(p)):
            if i>0 and (ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i]) - ord(p[i - 1]) == -25):
                cumu += 1
            else:
                cumu = 1

            if cumu > d.get(p[i], 0):
                d[p[i]] = cumu

        return sum([v for v in d.values()])

solu = Solution()
for p in ["", "z", "za", "abcdz"]:
    print(p, solu.findSubstringInWraproundString(p))