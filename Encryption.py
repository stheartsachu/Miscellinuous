import math
s = "haveaniceday"
print(len(s))

s_arr = []
for i in s:
    s_arr.append(i)

floor_value = math.floor(math.sqrt(len(s)))
ceil_value = math.ceil(math.sqrt(len(s)))

print(ceil_value,floor_value)
print(s_arr)

l = []

for i in range(floor_value):
    l.append([])
    for j in range(i*ceil_value, ceil_value*(i+1)):
        # print(i, j)

        l[i].append(s_arr[j])
ar1 = []
for i in range(ceil_value):
    ar1.append([])
    for j in range(floor_value):
        ar1[i].append(l[j][i])

ar2 = []
for i in ar1:
    ar2.append("".join(i))
print(' '.join(ar2))
