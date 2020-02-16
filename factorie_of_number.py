ar = [8 ,10]
n = 2
k = 2
counter = 0
l = []
check = []
for i in range(len(ar)):
    print(i)
    for j in range(i+1, len(ar)):
        print(j)
        var1 = ar[i], ar[j]
        if sum(var1) % k == 0:
            counter += 1
print(counter)
        # print(var1)
        # if var1 == var2:

        # try:
        #     if ar[i] != ar[j]:
        #         l.remove(var2)
        # except:
        #     pass
        # check.append(var2)

print(l)
for i in l:
    if sum(i) % k == 0:
        counter += 1
print(counter)

# new_list = []
# for a,b in l:
#     if a == b:
#         var = a,b
#         new_list.append(var)
#     if a != b:
#         var1 = a, b
#         var2 = b, a
#         # print(var1[0])
#         # print(var2[1])
#         # print(a)
#         # print(b)
#         l.remove(var2)
#         if var1[0] == var2[1] and var1[1] == var2[0]:
#             var3 = var1[0],var1[1]
#             print(var3)
#             # new_list.append(var3)
# print(sorted(new_list))
# # print(check)
# n_l = set(l)
# for i in n_l:
#     if sum(i) % k == 0:
#         counter += 1
# print(counter)
# nl = []
# for i in l:
#     if i not in l:
#         nl.append(i)
# print(l)
# print(nl)
# print(counter)
# final_list = []
# for num in l:
#     if num not in final_list:
#         final_list.append(num)
# print(len(final_list))

