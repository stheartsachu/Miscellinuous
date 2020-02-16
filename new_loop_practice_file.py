row = 3
ceil_value = 4
st = ['h', 'a', 'v', 'e', 'a', 'n', 'i', 'c', 'e', 'd', 'a', 'y']
var1 = 0
var2 = ceil_value
ecrtp_mat = []

lst = []
for i in range(ceil_value):
    lst.append([])
print(lst)

while True:
    n_ar = st[var1:var2]
    ecrtp_mat.append(n_ar)
    var1 = var2
    var2 += ceil_value
    if var2 > len(st):
        check = var2-len(st)
        if check != 0:
            l1 = var2-ceil_value
            l2 = var2 + check
            l3 = st[l1:l2]
            for i in range(len(l3)):
                lst[i].append(l3[i])
                # ecrtp_mat.append()
        break
print(lst)

for i in ecrtp_mat:
    if len(i) == 0:
        ecrtp_mat.remove(i)
print(ecrtp_mat)

final = []
for i in range(len(ecrtp_mat)):
    final.append([])
    final[i].append(ecrtp_mat)


print(final[0][0][0][0])
