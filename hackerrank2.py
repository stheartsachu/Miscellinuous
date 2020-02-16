grades = [73, 67, 38, 33]

upgaraded_grade = []
un_upgrades_grade = []

var_list = []

var_in_list = [[] for i in range(len(grades))]


for i in grades:

    if int(i) > int(38):
        var = int(i)
        var1 = "%s" % var
        for j in var1:
            var_list[i].append(j)

        var3 = "%s" % var_list[0]
        var4 = "%s" % var_list[1]
        var5 = int("%s%s" % (var3, var4))

        if int(var_list[1]) <= int("5"):

            var6 = int("%s5" % var_list[0])

            if var6-var5 < 3:
                upgaraded_grade.append(var6)

        if int(var_list[1]) >= int("5"):

            var7 = var_list[0]
            print(var7)
            var8 = int(var7)+1
            var9 = "%s0" % var8
            print(var9)

            if int(var9)-var5 > 3:

                un_upgrades_grade.append(var9)

    if int(i) <= int(38):
        un_upgrades_grade.append(i)

print(upgaraded_grade)
print(un_upgrades_grade)

for i, j in zip(upgaraded_grade, un_upgrades_grade):
    print(i)
    print(j)

