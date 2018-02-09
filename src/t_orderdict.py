# coding: utf8
"""
---------------------------------------------
    File Name: t_orderdict
    Description: 
    Author: wangdawei
    date:   2018/1/26
---------------------------------------------
    Change Activity: 
                    2018/1/26
---------------------------------------------    
"""

from collections import OrderedDict as odict

od = odict()
od["a"] = "3"
od["b"] = "1"
od["c"] = "2"
print(od)
print(od.pop("b"))
print(od.values())




