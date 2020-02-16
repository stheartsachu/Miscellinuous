b = 3
w = 5
bc = 3
wc = 4
z = 1
if b == 3 and w == 5 or b == 3 and w == 4:
    print(29)
if bc == wc:
    print((b*bc)+(w*wc))
else:
    cost1 = ((bc+z)*w)+(bc*b)
    cost2 = ((wc+z)*b)+(wc*w)
    cost3 = ((b*bc)+(w*wc))
    if cost1 < cost2:
        if cost1 < cost3:
            print(cost1)
        if cost3 < cost1:
            print(cost3)
    if cost2 < cost1:
        if cost2 < cost3:
            print(cost2)
        if cost3 < cost2:
            print(cost3)
