def fun():
    x1 = 1113
    v1 = 612
    x2 = 1331
    v2 = 610
  
    list1 = []
    list2 = []
    n = 1000000000

    for i in range(x1, n, v1):
        list1.append(i)

    print(list1)
    for j in range(x2, n, v2):
        list2.append(j)
    print(list2)
    def check():
        for var1, var2 in zip(list1, list2):
            while var1 == var2:
                return True
    if check() == True:
        return print("YES")
    else:
        return print("NO")

fun()
