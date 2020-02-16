def fun():
    grades = [73, 67, 38, 33]

    upgraded_list = []
    un_upgraded_list = []

    new_list = []

    final_list = []
    unmodified_list = []

    for i in grades:
        if i >= 38:
            upgraded_list.append(i)

        else:
            un_upgraded_list.append(i)

    for i in upgraded_list:
        while i % 5 != 0:
            i += 1
        new_list.append(i)

    for i, z in zip(new_list, upgraded_list):
        diff = i-z
        if diff < 3:
            final_list.append(i)
        if diff == 3:
            unmodified_list.append(z)
    unmodified_list.extend(un_upgraded_list)
    n_l = []
    for var1, var2 in zip(final_list, unmodified_list):
        n_l.append(var1)
        n_l.append(var2)
        final_list.extend(unmodified_list)
    print(final_list)

fun()

# string_list = []

# for j in upgraded_list:
#     var = str(j)
#     string_list.append(var)
#
# conversion_list = []
#
# for i in string_list:
#     var1 = i[0]
#     var2 = i[1]
#     var3 = "%s5" % var1
#     var4 = int(var3)
#     print(var4)
#     var7 = int(var1) + 1
#     var5 = "%s0" % var7
#     var6 = int(var5)
#     print(var6)
#
#     if int(i) > var4:
#         conversion_list.append(var4)
#     if int(i) < var6:
#         conversion_list.append(var6)

# print(string_list)
# print(conversion_list)
# print(upgraded_list)
# print(un_upgraded_list)

