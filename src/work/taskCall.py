# coding: utf8

import sys
import collections
import re

class taskCall:

    # for shell,
    def task2Graph(self, file):
        fileVisited = set([])
        que = collections.deque()

        que.append(file)
        fileVisited.add(file)
        g = {}

        while len(que) > 0:
            tmpfile = que.popleft()
            g.setdefault(tmpfile, collections.OrderedDict())
            print("#file#", tmpfile)
            tmpfr = open(tmpfile, 'r')
            variables = {}
            for line in tmpfr:
                line = line.strip().strip("\"")
                if line.startswith("#") or line.startswith("echo"):
                    continue

                if line.find("#") > 0:
                    line = line[:line.find("#")]

                vars = re.findall("\$[a-zA-Z_0-9]+", line)
                for var in vars:
                    # print("var: ",var, variables.get(var[1:], ""))
                    line=line.replace(var, variables.get(var[1:], ""), 1)
                    # print("var replace: ", line)

                declares = line.split(";")
                for dec in declares:
                    if dec.find("=") > 0:
                        ind = dec.find("=")
                        val = dec[ind + 1:].strip().strip("\"")
                        variables[dec[:ind]] = val
                        # print("variables: ", dec[:ind], val)

                segs = line.split()
                for seg in segs:
                    if re.match("^[^\"\'].*(sh|py|pl)$", seg):
                        if seg not in fileVisited:
                            que.append(seg)
                            fileVisited.add(seg)


                        calls = g.get(tmpfile)
                        calls[seg] = True
            tmpfr.close()

        stack = []
        stack.append((file, 0))
        while len(stack)>0:
            scrtips, tabs = stack.pop()

            calls = list(g[scrtips].keys())
            if calls is not None and len(calls) > 0:
                calls.reverse()
                for c in calls:
                    stack.append((c, tabs+1))

            print("%s%s" % ("\t"*tabs, scrtips))


if __name__ == "__main__":
    file = sys.argv[1]
    taskcall = taskCall()
    taskcall.task2Graph(file)




