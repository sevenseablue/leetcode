
class Solution:
    # @param tokens, a list of string
    # @return an integer

    def ceil(self, x):
        if x == int(x):
            return int(x)
        else: return int(x)+1

    def isOperSym(self, token):
        if token == "+" or token == "-" or token == "*" or token == "/":
            return True
        else:
            return False

    def evalRPN(self, tokens):
        operNum = []
        for t in tokens:
            if not self.isOperSym(t):
                operNum.append(t)
            else:
                num2 = int(operNum.pop())
                num1 = int(operNum.pop())
                if t == "+":
                    operNum.append((num1 + num2))
                elif t == "-":
                    operNum.append((num1 - num2))
                elif t == "*":
                    operNum.append((num1 * num2))
                elif t == "/":
                    if num2 != 0:
                        num3 = int(num1 *1.0 / num2)
                        operNum.append(num3)
                    else:
                        return None
#                        raise Exception("divided by zero.")
                else:
                    operNum.append(t)
        return int(operNum.pop())


tokens = [
    ["18"],
    ["2", "1", "+"],
#    ["2", "0", "/"],
    ["2", "1", "+", "3", "*"],
    ["2", "1", "3", "*", "+"],
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
    ["4","-2","/","2","-3","-","-"],
    ["6","9","3","+","-11","*","/"]
]
solu = Solution()
for t in tokens:
    print solu.evalRPN(t)

# 18
# 3
# 9
# 5
# 22
# -7

