# coding: utf8
"""
---------------------------------------------
    File Name: randomseq
    Description: 
    Author: wangdawei
    date:   2018/3/15
---------------------------------------------
    Change Activity: 
                    2018/3/15
---------------------------------------------    
"""


import random as r


def rs(n):
    seqs = list(range(n))
    res = []
    while len(seqs)>=1:
        ind = r.randint(0, len(seqs)-1)
        res.append(seqs[ind])
        # seqs.remove(seqs[ind])
        seqs.pop(ind)
    spain = {0, 1, 2, 3}
    for i in range(int(n/2)):
        if res[i*2] in spain and res[i*2+1] in spain:
            return 1
    return 0

num = 0
times = 10000
for i in range(times):
    num += rs(8)

print(num, times, num/times)


print(1-8/35)