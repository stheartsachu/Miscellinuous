
arr = [24 ,29 ,70 ,43 ,12 ,27, 29 ,24 , 12 ,41 ,43 ,24 ,70 ,24 ,100 ,41 ,43 ,
       43 ,100 ,29 ,70 ,100 ,43 ,41 ,27 ,70 ,70 ,59 ,41 ,24 ,24 ,29,
       43, 24 ,27 ,70 ,24, 27 ,70 ,24, 70, 27, 24, 43, 27 ,100, 41, 12, 70,
       43 ,70 ,62 ,12 ,59 ,29 ,62 ,41 ,100 ,43 ,43 ,59 ,59 ,70 ,12 ,27 ,43 ,43 ,27 ,27 ,27 ,
       24 ,43 ,43 ,62 ,43 ,70, 29]
n_arr = list(set(arr))
print(n_arr)

count = []
for i in n_arr:
    var = [i,arr.count(i)]
    count.append(var)
# print(count)
count.remove(max(count,key=lambda x: x[1]))
print(max(count,key=lambda x: x[1]))
# print(count)
counter = 0
for i in count:
    counter += i[1]
print(counter)
