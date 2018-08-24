import os, jpype
jarpath = "/home/wangdawei/github/algs4/target/algs4-1.0.0.0.jar"
jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jarpath)
AcycleLPSort = jpype.JClass('edu.princeton.cs.algs4.AcycleLPSort')
# IntDouble = jpype.JClass('edu.princeton.cs.algs4.IntDouble')
acycleLPSort = AcycleLPSort()
res = acycleLPSort.sort("/home/wangdawei/github/algs4/algs4-data/tinyEWD.nocycle.txt")
# l1 = [(IntDouble.parseI(e), IntDouble.parseD(e)) for e in res]
l2 = [(e.i, e.d) for e in res]
# l3 = [e for e in res]
jpype.shutdownJVM()
# print(l1)
print(l2)
# print(l3)