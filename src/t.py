# coding: utf8
"""
---------------------------------------------
    File Name: t
    Description: 
    Author: wangdawei
    date:   2018/1/11
---------------------------------------------
    Change Activity: 
                    2018/1/11
---------------------------------------------    
"""


import re
import numpy as np

def t():
    print([(m.start()) for m in re.finditer("ab.", "abcabdabea")])
    print(np.argsort([1,1,2,1,2,3]))
    pass

if __name__ == "__main__":
    t()
