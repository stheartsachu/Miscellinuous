l = [1, 2, 3, 4]
set = []
for i in range(len(l)):
    l2 = []
    # print(l[i])
    l2.append(l[i])
    for j in range(i+1, len(l)):
        print()
        l2.append(l[j])
    set.append(l2)
    del l2
print(set)

