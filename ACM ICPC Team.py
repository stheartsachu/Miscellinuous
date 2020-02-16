topic = ['10101', '11100', '11010', '00101']
ar = []
for i in range(1, len(topic)+1):
    ar.append(i)
ar2 = []
# for i in range(len(ar)):
#     for j in range(len(ar)):
#         if ar[i] != ar[j]:
#             if [ar[j], ar[i]] not in ar2:
#                 ar2.append([ar[i], ar[j]])
for i in range(len(topic)):
        for j in range(i+1,len(topic)):
                ar2.append([ar[i],ar[j]])
print(ar2)
ar3 = []
for i in ar2:
    var = int(topic[i[0]-1]) + int((topic[i[1]-1]))
    ar3.append(str(var))

count = 0
counter = []
counter2 = []
for i in ar3:
    for j in i:
        if j != "0":
            count += 1
    counter.append(count)
    counter2.append(str(count))
    count = 0

print((max(counter)), counter2.count(str(max(counter))))

