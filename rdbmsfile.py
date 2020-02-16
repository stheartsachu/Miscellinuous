    n = int(input())
    l = []
    score_list = []
    for i in range(n):
        l.append([])
    for j in l:
        j.insert(0,input())
        j.insert(1,float(input()))

    m_l = []
    n_l = []
    for i in l:
        m_l.append(i[1])
        n_l.append(i[0])
    sorted(m_l)
    print(m_l)
    # n = len(m_l)
    # for var1 in range(n):
    #     for j in range(0, n-var1-1):
    #         if m_l[j] > m_l[j+1] :
    #             m_l[j], m_l[j+1] = m_l[j+1], m_l[j]

    n2 = len(m_l)-1
    max_element = []
    max_element_names = []
    max_element.append(m_l[0])
    max_element_names.append(n_l[0])

    for i in range(1,n2):
        if m_l[0] == m_l[i]:
            max_element.append(m_l[i])
            max_element_names.append(n_l[i])

    # for i in range(len(max_element_names)-1):
    #     print(min(max_element_names[0],max_element_names[i]))

    for i in max_element:
        m_l.remove(i)

    n3 = len(m_l)-1
    second_most_element = []
    second_most_element_names=[]
    second_most_element_names.append(n_l[0])
    second_most_element.append(m_l[0])
    for i in range(0,n3):
        if m_l[0] == m_l[i]:
            second_most_element.append(m_l[i])
            second_most_element_names.append(n_l[i])
    print(second_most_element)
    print(second_most_element_names)
    #  now we will find the index of greatest and second greatest

    mergedlist = list(set(second_most_element_names))
    f_l = sorted(mergedlist)
    for i in f_l :
        print(i)

    # n3 = len(mergedlist)-1
    # f_l =[]
    # for i in range(n3):
    #     x = min(mergedlist[i],mergedlist[i+1])
    #     y = max(mergedlist[i],mergedlist[i+1])
    #     f_l.append(x)
    #     f_l.append(y)
    # for i in f_l:
    #     print(i)
