arr = [5 , 4 ,4  ,2 ,2 ,8]
min_element = min(arr)
stack = [[5 , 4 ,4  ,2 ,2 ,8]]
l = []
for j in range(4):
    list_counter = stack.pop()
    print(list_counter)
    for i in list_counter:
        if i != min_element:
            print(i)
            l.append(i-min_element)
    stack.append(l)


    # print(stack)
