p = [4, 3, 5, 1, 2]

l = []
for i in range(1, len(p)+1):
    l.append(i)

l2 = []
for i in range(len(l)):
    for j in range(len(l)):
        index = p[j]
        index2 = p[index-1]
        if index2 == l[i]:
            l2.append(p[j])
l3 = []
for i in l2:
    var = p.index(i)
    l3.append(var+1)

