import random
ar = []
n_c_blow = []
n_ar = []

for x in range(1000000):
  ar.append(random.randint(1, 21)*5,) #random.randint(1,21)*5,

for i in ar:
    n_ar.append(i)
    if i == max(ar):
        n_c_blow.append(i)

if ar == n_ar:
    print(sum(ar))
if ar != n_ar:
    print((len(n_c_blow)))



# c_ar = ar.copy()
# ar_set = set(ar)
# c_ar_set = set(c_ar)
#
# res = ar_set | c_ar_set
#
# res2 = list(res)
#
# if len(res2) == 1:
#     print("Elements are same ")
# else :
#     print("Elements are diff ")
