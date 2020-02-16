l = [2, 4, 8, 2, 3, 5, 1, 7, 9, 6]
sum = 14
final = []
for i in range(len(l)):
    curr_sum = l[i]
    j = i+1
    while j <= len(l):
        if curr_sum == sum:
            # print(l[i:j])
            final.append(l[i:j])

        if curr_sum > sum or j == len(l):
            break
        curr_sum = curr_sum + l[j]
        j += 1
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i]+l[j] == 14:
            # print(l[i],l[j])
            final.append([l[i],l[j]])
print(final)
