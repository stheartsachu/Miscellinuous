arr = [5 ,4 ,4 ,2 ,2 ,8]
res = []
min_element = min(arr)
min_v = []
for j in range(1):
    for i in range(len(arr)):
        if arr[i] != min_element:
            # var = arr[i]-min_element
            arr.insert(i, arr[i])
            arr.pop(i+1)
        if arr[i] == min_element:
            # arr.insert(i, 0)
            arr.pop(i+1)
    res.append(max(arr))
    temp_list = []
    temp_list1 = []
    for i in arr:
        if i != 0:
            temp_list.append(i)
    min_v.append(min(temp_list))
    # print(min_v[-1])
    min_element = min_v[-1]

# print(min_element)
# print(arr)
print(res)

