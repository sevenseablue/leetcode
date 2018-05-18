class Solution:
    def min_my(self, nums, s, e):
        minv = 2**31
        minvind = -1
        for i in range(s, e+1):
            if nums[i]<minv:
                minv = nums[i]
                minvind = i

        return minv, minvind

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return "0"
        n = len(num)
        nums = [int(n) for n in num]
        result = []
        s = 0
        for i in range(n-k):
            if i == 0:
                v, ind = self.min_my(nums, s, i+k)
            else:
                v, ind = self.min_my(nums, s, i + k)
            s = ind + 1
            result.append(str(v))

        return str(int("".join(result)))

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return "0"
        stack = []
        cnt = 0
        for i, ch in enumerate(num):
            if cnt == k:
                for j in range(i, len(num)):
                    stack.append(num[j])
                break
            if not stack or ch >= stack[-1]:
                stack.append(ch)
            else:
                while stack and ch < stack[-1] and cnt < k:
                    stack.pop()
                    cnt += 1
                stack.append(ch)
        while cnt < k:
            stack.pop()
            cnt += 1
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        if i == len(stack):
            return "0"
        return ''.join(stack[i:])

solu = Solution()
num = "1432219"
k = 3
num = "10200"
k = 1
# num = "10"
# k = 2
print(solu.removeKdigits(num, k))


