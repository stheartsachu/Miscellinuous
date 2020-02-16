s = [1, 2, 1, 3, 2]
d = 29
m = 12
sum = 0

new_list = []
for i in range(len(s)-1):
    var1 = s[i]
    var2 = s[i+1]
    var3 = int(var1+var2)
    print(var3)
    if var3 == d:
        new_list.append(i)
print(new_list)

# for j in s:
#     print(j)
# # pick those elements whose sum is 29 and elements are selectd in such a way that length of array remains
