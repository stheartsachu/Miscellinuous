arr = ["Harsh","Beria","Varun","Kakunami","Vikas"]

arr1 = [20, 20, 19, 19, 21]


s_rade = [[i, j] for i, j in zip(arr, arr1)]
s_rade.sort(key=lambda x: x[1])

s_h_n = []
for i in range(len(s_rade)):
    s_h_n.append(s_rade[i][1])
s_h_n_set = list(set(s_h_n))

second_last = []
for i in range(len(s_rade)):
    if s_h_n_set[1] == s_rade[i][1]:
        second_last.append(s_rade[i])
second_last.sort(key=lambda x: x[0])

for i in range(len(second_last)):
    print(second_last[i][0])
