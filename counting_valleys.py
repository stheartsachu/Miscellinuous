# n = 8
s = "UDUUUDUDDD"

print(s.count("U"))

print(s)

ar = []
for i in s:
    ar.append(i)
n_ar = []
for i in range(1,len(ar)-1):
    n_ar.append(ar[i])
print(n_ar)
var = len(n_ar)-1
counter = 0
u_count = 0
d_count = 0
if s.count("U") == s.count("D"):
    for i in range(var):
        if n_ar[i] == "U" and n_ar[i+1] == "D":
            # print(n_ar[i])
            # print(n_ar[i+1])
            counter += 1
        if n_ar[i] == "U":
            u_count += 1
        if n_ar[i] == "D":
            d_count += 1
            # for i in range(i, -1, -1):
            #     if n_ar[i] == "U":
            #         print(n_ar[i])
            #         u_count += 1

    print(u_count)
    print(d_count)

    print(counter)
else:
    print(0)

