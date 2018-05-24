
class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def gen_list(ind, stack, ln, rn):
            if ln>n or rn > n or rn > ln:
                return
            if ind == 2*n and ln==n and rn == n:
                result.append("".join(stack))
            stack.append("(")
            gen_list(ind+1, stack, ln+1, rn)
            stack.pop()
            stack.append(")")
            gen_list(ind+1, stack, ln, rn + 1)
            stack.pop()

        def gen_str(ind, stack, ln, rn):
            if ln > n or rn > n or rn > ln:
                return
            if ind == 2 * n and ln == n and rn == n:
                result.append(stack)
            gen_str(ind + 1, stack + "(", ln + 1, rn)
            gen_str(ind + 1, stack + ")", ln, rn + 1)
        gen_str(0, "", 0, 0)
        return result

solu = Solution()
for i in range(5):
    print(solu.generateParenthesis(i))
