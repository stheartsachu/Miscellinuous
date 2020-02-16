# l = []
# l2  = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# rng1 = 3
# rng2 = 4
# for i in range(rng1):
#     l.append([])
#     for j in range(i*rng2, rng2*(i+1)):
#         l[i].append(l2[j])
# print(l)
l3 = [['h', 'a', 'v', 'e'], ['a', 'n', 'i', 'c'], ['e', 'd', 'a', 'y']]
ar1 = []
for i in range(4):
    ar1.append([])
    for j in range(3):
        ar1[i].append(l3[j][i])

for i in ar1:
    st = "".join(i)
    print(st)

        # print(l3[i][j])
# l4 = []
# break_point = 0
# i = -1
# j = 0
# while True:
#     # print(j)
#     if i != -1:
#         print(l3[i][j])
#     i += 1
#     j += 1
#     if i == len(l3):
#         break


# for i in range(len(l3[0])):
#     print(l3[i][i])
