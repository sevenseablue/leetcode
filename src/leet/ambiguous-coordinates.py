# coding: utf8
"""
---------------------------------------------
    File Name: ambiguous-coordinates
    Description: 
    Author: wangdawei
    date:   2018/4/16
---------------------------------------------
    Change Activity: 
                    2018/4/16
---------------------------------------------    
"""


def digit_valid_list(digit):
    result = []
    for ind in range(1, len(digit)+1):
        if 1 <= ind < len(digit):
            original_digit = digit[0:ind] + "." + digit[ind:]
        else:
            original_digit = digit

        if is_digit_valid(original_digit):
            result.append(original_digit)

    return result


def is_digit_valid(original_digit):
    dot_index = original_digit.find(".")
    if dot_index<0:
        if len(original_digit)>1 and original_digit[0] == "0":
            return False
    else:
        if original_digit[-1] == "0":
            return False
        elif dot_index>1 and original_digit[0] == "0":
            return False
        elif dot_index<1:
            return False

    return True


class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        s = S[1:len(S)-1]
        result = []
        for i in range(1, len(s)):
            s1, s2 = s[0:i], s[i:]
            l1, l2 = digit_valid_list(s1), digit_valid_list(s2)
            # print(s1, l1, s2, l2)
            if len(l1)>0 and len(l2)>0:
                result.extend(["(%s, %s)" % (e1, e2) for e1 in l1 for e2 in l2])
            pass
        return result



for original_digit in ["00", "0.0", "0.00", "1.0", "001", "00.01", ".1"]:
    print(original_digit, is_digit_valid(original_digit))

solu = Solution()
for digit in ["(123)", "(00011)", "(0123)", "(100)", "(00)", "(000)"]:
    print(solu.ambiguousCoordinates(digit))