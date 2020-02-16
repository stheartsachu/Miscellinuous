n = int(input())
string_list = []
d_list = [[]]*n
for i in range(n):
    string_list.append(str(input()))


for i in string_list:
    for j in range(len(i)):
        if j % 2 == 0:
            d_list[0].append(i[j])
for i in string_list:
    for j in range(len(i)):
        if j % 2 != 0:
            d_list[0].append(i[j])


for i in range(n):
    string_list.append(str(input()))

for j in range(n):
    if j % 2 == 0:
        for i in string_list:
            d_list[j].append(i[j])
    if j % 2 != 0:
        for i in string_list:
            d_list[j].append(i[j])

print(d_list)

word ="string"
print(word[::2])
print(word[1::2])
l = [1,3,3232,232,22,11]
print(l[:2])

