

import json
machs = []
for i in range(1, 6):
    print(i)
    path1 = "/home/wangdawei/Qunar/projects/hadoop/c%s.txt" % i
    text = open(path1, 'r').read()
    if text.startswith(u'\ufeff'):
        text = text.encode('utf8')[3:].decode('utf8')
    d=json.loads(text)

    for obj in d["data"]["alerts"]:
        machs.append((obj["contacts"], obj["name"], obj["path"]))
print(len(machs))
l1 = []
l2 = []
for m in sorted(machs):
    if m[2].find("qunar.team.data") <0:
        l1.append(m[1:])

    else:
        l2.append(m[1:])
print(len(l1))
print(len(l2))
for e in l1:
    print(e)