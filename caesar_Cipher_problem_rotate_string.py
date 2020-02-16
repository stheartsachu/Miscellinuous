s = ""
k = 0
o_s = "abcdefghijklmnopqrstuvwxyz"
n_k = 0
if k > len(o_s):
    while True:
        n_k += 26
        if n_k > k:
            n_k -= 26
            break
    k = k-n_k
n_s = s.lower()
ar = []
for i in o_s:
    ar.append(i)
s_p = []
for i in range(k):
    s_p.append(ar[i])
f_p = []
for i in range(k, len(o_s)):
    f_p.append(ar[i])
final = f_p+s_p

ar1 = []
for i in range(len(o_s)):
    if ar[i] in n_s:
        ar1.append([i, ar[i]])
ar2 = []
for i in ar1:
    ar2.append(i[1])
st = []
for i in s:
    if i.islower() == True:
        n_i = i.lower()
        if n_i in ar2:
            index = ar2.index(n_i)
            f_index = ar1[index][0]
            st.append(final[f_index])
    if i.isupper() == True:
        n_i = i.lower()
        if n_i in ar2:
            index = ar2.index(n_i)
            f_index = ar1[index][0]
            st.append(final[f_index].upper())
    if i not in ar2:
        if i.isalpha() != True:
            st.append(i)

e_p = "".join(st)
print(e_p)
