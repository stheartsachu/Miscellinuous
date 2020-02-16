c = 5
m = 2
res = c
r_wraper = 0
while True:
    n_c = c//m
    print(c)
    c = n_c


    res += n_c
    r_wraper = c-(n_c*m)
    if c < m:
        res += c
        break

print(res)
print(n_c)
print(r_wraper)

# print("quotient %s "%(c//m) )
# print("remainder %s " % (c%m))
