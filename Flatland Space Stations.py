n = 20
m = 5

if m == 1:
    print(n-1)
elif m == n:
    print(0)
else:
    f_p = []
    s_p = []
    var = 0
    for i in range(m, 0, -1):
        print(i)
        f_p.append(i-1)
    for i in range(m+1, n+1):
        print(i)
        var += 1
        s_p.append(i-var)
    print(f_p)
    print(s_p)
    m_p = f_p + s_p
    print(m_p)
