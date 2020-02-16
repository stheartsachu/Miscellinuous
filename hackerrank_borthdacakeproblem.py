s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
d = 3
m = 2
s_len = 0
if len(s) > 1:
    s_len = len(s)-1
if len(s) == 1:
    s_len = len(s)
var_list1 = []
var_list2 = []
var_list3 = []
for i in range(s_len):
    var = s[i]
    var_list1.append(var)
    v = 0
    if len(s) > 1:
        var2 = s[i+1]
        var_list2.append(var2)
    if len(s) == 1:
        var_list2.append(0)

print(sum(var_list1))

sum_list = []
for i, j in zip(var_list1, var_list2):
    sum_list.append(i+j)
counter = 0
for var in sum_list:
    if var == d:
        counter += 1
print(counter)

