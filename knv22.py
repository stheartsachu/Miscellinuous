l = [2, 4, 8, 2, 3, 5, 1, 7, 9, 6]  # input array
sum = 14  # result

l1 = []
for i in range(len(l)):
    l1.append([])
    l1[i].append(l[i])
    for j in range(i, len(l)):
        l1[i].append(l[j])
print(l1)
l2 = []
value = 0
for i in l1:
    l3 = []
    value = i[0]
    # print(i[0])
    l3.append(i[0])
    for j in range(1, len(i)):
        # print(i[j])
        value += i[j]
        if value < sum:
            l3.append(j)
        if value > sum:
            value -= j
    print(l3)
    l2.append(l3)
    l3.clear()
print(l2)
