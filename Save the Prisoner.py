l = [0 ,9, 2, 5, 8, 5, 0, 1, 3, 2, 7, 4 ,8 ,4]
sum = 12
res = []
for i in l:
    if i == sum:
        res.append([i])
if len(res) == 0:
    for j in range(len(l)):
        for k in range(j+1, len(l)):
            if l[j] + l[k] == sum:
                res.append([l[j], l[k]])
if len(res) == 0:
    for j in range(len(l)):
        for k in range(j+1, len(l)):
            for p in range(j+2, len(l)):
                if l[j] + l[k] + l[p] == sum:
                    res.append([l[j], l[k], l[p]])
unique_data = [list(x) for x in set(tuple(x) for x in res)]
if len(res)==0:
    print("no subarry match the condition")
else:
    print(unique_data[0])
