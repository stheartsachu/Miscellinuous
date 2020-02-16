# arr = [66 ,42 ,68 ,72 ,68 ,81 ,91 ,19 ,40 ,73 ,44 ,73 ,89 ,73 ,44 ,12 ,77 ,40 ,44 ,17 ,59 ,99 ,35 ,92 ,80 ,51 ,14 ,30]
# res = [len(arr)]
# min_value = min(arr)
# j = 0
# while True:
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[i] = arr[i]-min_value
#         if arr[i] == 0:
#             arr[i] = 0
#     m_arr = arr
#     m_arr2 = []
#     for i in m_arr:
#         if i > 0:
#             m_arr2.append(i)
#     if len(m_arr2) == 0:
#         break
#     min_value = min(m_arr2)
#     del m_arr2
#     counter = 0
#     for i in arr:
#         if i != 0:
#             counter += 1
#     res.append(counter)
# print(res)
# print(arr)
l=[[4, 9, 2], [3, 5, 7], [8, 1, 5]]
d1=0
d2=0
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
j=[]
for i in range(0,3):
    d1=d1+l[i][i]
    j.append(d1)
    d2=d2+l[-i][i]
    j.append(d2)
    r1=r1+l[0][i]
    j.append(r1)
    r2=r2+l[1][i]
    j.append(r2)
    r3=r3+l[2][i]
    j.append(r3)
    c1=c1+l[i][0]
    j.append(c1)
    c2=c2+l[i][1]
    j.append(c2)
    c3=c3+l[i][2]
    j.append(c3)


print(max(j))

for i in range(0,2):
    if(d1==15 and d2==15):





