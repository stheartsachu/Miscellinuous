l = [2, 4, 8, 2, 3, 5, 1, 7, 9, 6]

# print(len(l))
sum = 14
j = 1
while True:
    j += 1
    # print(j)
    i = j
    index1 = 0
    index2 = j
    while True:
        # i += 0
        index1 += i
        index2 += i
        print(index1, index2)
        if index2 >= len(l):
            break

    if j >= len(l):
        break

# i = 1
# index1 = 0
# index2 = 2
# while True:
#     i += 1
#     print(index1, index2)
#     index1 += i
#     index2 += i
#     if index2 >= len(l):
#         break
