n = 100
num = 5
arr = [50, 10, 20, 30, 40]
def robert(n,num,arr):

    l = []
    l1 = []

    counter = 0
    for i in range(0, len(arr), 2):
        print(arr[i])
        l.append(arr[i])
    for j in range(1, len(arr), 2):
        l1.append(arr[j])

    counter = 0
    l2 = []
    for i in l:
        for j in l:
            counter=i+j
            if counter<100:
                if counter not in l2:
                    l2.append(counter)



    print(l2)

        # if counter < n:
        #     print(arr[i])
        #     l.append(counter)

        #     print(counter)


    # l = []
    # for i in range(num):
    #     l.append([])
    #
    # for i in range(num):
    #     for j in range(
    #     num):
    #         print(arr[i], arr[j])
            # l[i].append(arr[i])
    # for i in l:
    #     print(i)
    # print(l)
    print(l)
    print(l1)
robert(n,num,arr)
