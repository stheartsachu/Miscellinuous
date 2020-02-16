arr = [1 ,4 ,4 ,4 ,5 ,3]
l = []
for i in arr:
    var = arr.count(i)
    var2 = i, var
    l.append(var2)

nl = []
print(l)
s_l = set(l)

sorted(s_l, key=lambda item: item[1])
print(s_l)
# length = len(s_l)

for i in range(len(s_l)):
    pass



# l = []
# k=0
# g=0
# arr.sort()
# for i in arr:
#     if i not in l:
#         l.append(i)
# for i in l :
#     m=arr.count(i)
#     if m>k:
#         k=m
#         g=i
#
# print(g)
