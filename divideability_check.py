c = 5
m = 2
c_wraper = c
r_wraper = c_wraper
res = c
final = []
while True:
    c_wraper //= m
    print(c_wraper)
    res += c_wraper

    condition = c_wraper*c_wraper

    c_wraper += r_wraper-condition
    r_wraper = c_wraper

    final.append(c_wraper)
    if c_wraper < m:
        break
print(sum(final))
# print(res)

# print(res)
# print(r_wrapr)
# if condition < m:
#     pass
#
#
# qu = 27
# m = 7
# wrpr_count = 0
# while True:
#     qu = qu // m
#     # print(qu)
#     wrpr_count += qu
#     if qu < m:
#         wrpr_count += qu
#         break
# print(wrpr_count)
# print(26//7)
