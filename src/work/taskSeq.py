# coding: utf8


import sys
import os, jpype

class taskSeq:

    def file2tasks(self, f1):
        fr = open(f1, 'r')
        tasks = []
        for line in fr:
            line = line.rstrip("\n")
            arr2 = line.split("\t")
            # path, params, tbin, tbout, time, line
            tasks.append(
                (arr2[0], arr2[2], arr2[5].split(",") if arr2[5] else [], arr2[6].split(",") if arr2[6] else [], float(arr2[7]), line))
        fr.close()
        out2id=dict([(ot, t[0]) for t in tasks for ot in t[3]])
        id2time=dict([(t[0], t[4]) for t in tasks])
        id2time["_end_"] = 0.0
        edges=[(out2id[it], t[0], id2time[out2id[it]]) for t in tasks for it in t[2]]
        edges += [(t[0], "_end_", id2time[t[0]]) for t in tasks]

        vs = [id for id in id2time.keys()]
        id2i = dict([(id, i) for i, id in enumerate(vs)])
        edges2A4 = [(id2i[e[0]], id2i[e[1]], e[2]) for e in edges]
        graphfile = f1 + ".graph"
        graphfw = open(graphfile, 'w')
        graphfw.write("%s\n" % len(id2i))
        graphfw.write("%s\n" % len(edges2A4))
        [graphfw.write("%s %s %s\n" %(e[0], e[1], e[2])) for e in edges2A4]
        graphfw.close()

        jarpath = "/home/wangdawei/github/algs4/target/algs4-1.0.0.0.jar"
        jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jarpath)
        AcycleLPSort = jpype.JClass('edu.princeton.cs.algs4.AcycleLPSort')
        acycleLPSort = AcycleLPSort()
        res = acycleLPSort.sort(graphfile)
        i2v = dict([(e.i, e.d) for e in res])
        jpype.shutdownJVM()

        return [(id, status, ins, outs, runtime, i2v[id2i[id]], line) for id, status, ins, outs, runtime, line in tasks]

    def toRun(self, tasks):
        print(tasks)
        sucs = set([])
        [sucs.update(outs) for id, status, ins, outs, runtime, lptime, line in tasks if status == "success"]
        toRuns = [(lptime, line) for id, status, ins, outs, runtime, lptime, line in tasks if
                  status == "notStart" and sucs.union(ins) == sucs]
        print(toRuns)
        return [e[1] for e in sorted(toRuns, reverse=True)]

    def tasksToFile(self, tasks, file):
        fw = open(file, 'w')
        for line in tasks:
            fw.write("%s\n" % line)
        fw.close()

    def seq(self, tasks):
        # task, in, out
        sucs = set([])
        tabs = 0
        while True:
            runningSet = []
            tempTasks = []
            for task, ins, outs in tasks:
                insSet = set(ins)
                if insSet.intersection(sucs) == insSet:
                    runningSet.append((task, ins, outs))
                else:
                    tempTasks.append((task, ins, outs))
            if runningSet:
                for task, ins, outs in runningSet:
                    print("%srun %s..." % ("\t" * tabs, task))
                    sucs.update(outs)
            else:
                if tasks:
                    raise Exception("%s can not run." % tasks)
                else:
                    break
            tabs += 1
            tasks = tempTasks
        pass


tseq = taskSeq()
tasks = tseq.file2tasks(sys.argv[1])
toRuns = tseq.toRun(tasks)
tseq.tasksToFile(toRuns, sys.argv[1] + ".toRun")
