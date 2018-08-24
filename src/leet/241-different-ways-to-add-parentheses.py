# coding: utf8
"""
---------------------------------------------
    File Name: 241-different-ways-to-add-parentheses
    Description: 
    Author: wangdawei
    date:   2018/4/18
---------------------------------------------
    Change Activity: 
                    2018/4/18
---------------------------------------------    
"""


def computer(i1, oper, i2):
    return {"*": lambda x,y: x*y,
     "+": lambda x,y: x+y,
     "-": lambda x,y: x-y}.get(oper)(i1, i2)

def computer_str(str1):
    stack = []
    oper_set = set(["+", "-", "*"])
    str_in = re.findall(r"(\*|\+|\-|\(|\)|\d+)", str1)
    shu = re.compile("-?\d+")
    # print(str_in)
    for i in range(len(str_in)):
        stack.append(str_in[i])
        l_s = len(stack)
        # print("l_s", l_s, stack)
        while l_s>=5 and stack[l_s-1] == ")" and stack[l_s-5] == "(" and (stack[l_s - 3] in oper_set) and re.match(shu, stack[l_s - 2]) and re.match(shu, stack[l_s - 4]):
            temp = computer(int(stack[l_s - 4]), stack[l_s - 3], int(stack[l_s - 2]))
            # print("temp, ", temp)
            # print("stack.pop 5 times")
            for i in range(5):
                stack.pop()
            stack.append(str(temp))
            # print("stack,", stack)
            l_s = len(stack)
            pass

    if len(stack) == 1:
        return stack[0]
    else:
        raise "error"



from itertools import permutations
import re
import copy
class Solution:
    def countPare(self, str, pare):
        if pare == "(":
            for i in range(len(str)):
                if str[i] != "(":
                    return i
        if pare == ")":
            for i in range(len(str)):
                if str[len(str)-1-i] != ")":
                    return i
        return 0
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        str_in = re.split(r"(\*|\-|\+)", input)
        # print(str_in)
        l_in = len(str_in)
        oper_order = list(permutations([ 2*i+1 for i in range(int(l_in/2))]))
        result = set([])
        # print(oper_order)
        for oper_or in oper_order:
            input2 = copy.copy(str_in)
            for oper in oper_or:
                n1, n2 = oper-1, oper+1
                lpare_num, rpare_num = 0, 0
                for i in range(n1, -1, -2):
                    lpare_num += self.countPare(input2[i], "(")
                    rpare_num += self.countPare(input2[i], ")")
                    if lpare_num == rpare_num:
                        input2[i] = "(" + input2[i]
                        break
                lpare_num, rpare_num = 0, 0
                for i in range(n2, l_in+1, 2):
                    lpare_num += self.countPare(input2[i], "(")
                    rpare_num += self.countPare(input2[i], ")")
                    if lpare_num == rpare_num:
                        input2[i] = input2[i]+")"
                        break
            result.add("".join(input2))
            # print(oper_or, "".join(input2))

        # print(result)
        result_f = []
        for r in result:
            result_f.append(int(computer_str(r)))
        return result_f



solu = Solution()
for input in  ["2-1-1",
         "2*3-4*5"]:
    solu.diffWaysToCompute(input)
