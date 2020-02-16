l = [1 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,0]
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0
j=0
k = 3
w=1
e=100
x=[]
while True:
    x.append(l[i])
    if l[i]==0:
        e=e-1-k
    if l[i]==1:
        e = e-1
    i=i+k
    j=j+1
    m=j*k
    if i >=len(l)-1:
        i=m-(w*(len(l)))
        w=w+1
        if i==0:
            x.append(l[0])
            if l[i]==0:
                e=e-1-k
            if l[i]==1:
                e = e-1
            break

print(x)
print(e)
    # print(l)
    # for i in l:
    #     if c[i-1] == 0:
    #         e = e-1-k
    #         print(e)
    #     if c[i-1] == 1:
    #         e = e-1
    #         print(e)
    # return e
