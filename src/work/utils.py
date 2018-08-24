

import hashlib

user = 'jointwisdom'
pwd = 'wdw0126mamaniuniu'

m2 = hashlib.md5()
m2.update(pwd.encode("utf-8"))
print(m2.hexdigest())

# 04411e944be30d3cffcea72eed894c5a