import numpy as np
list1 = [2, 4, 8, 2, 3, 5, 1, 7, 9, 6]
sum = 14
sublist = []
sum_list = []
c = []
for i in range(len(list1) + 1):
    for j in range(i+1,len(list1) + 1):
        sub = list1[i:j]
        sublist.append(sub)
        sum_ar = int(np.sum(sub))
        if sum_ar == sum:
            sum_list.append(sub)
        # c.append()

print(sublist)
print(sum_list)
ll = []
var = 0
for i in sublist:
    for j in i:
        var += j
    ll.append(var)
    var = 0
print(ll)
final = []
for i in range(len(ll)):
    if ll[i] == sum:
        final.append(i)
print(final)

