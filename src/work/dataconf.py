# coding: utf8

class dataconf:
    pass

file="dataconf.sh"
fr=open(file, 'r')
for line in fr:
        line = line.strip()
        exportind = line.find("export")
        if exportind != 0:
                continue
        nv=line[6:].strip()
        equalind = nv.find("=")
        if equalind>0:
                setattr(dataconf, nv[:equalind], nv[equalind+1:])

