
from random import randint
ar = []
n_c_blow = []
n_ar = []
for i in ar:
    n_ar.append(i)
    if i == max(ar):
        n_c_blow.append(i)

if ar == n_ar:
    print(sum(ar))
if ar != n_ar:
    print((len(n_c_blow)))
# for i in range(1000):
#     ar = [randint*i]
#
#     a = ar.count(ar[0])
#     print(a)
#     if a == len(ar):
#         print(a)
#     else:
#         print("hi")
