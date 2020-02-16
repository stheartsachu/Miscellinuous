# print(n)
n = 4
count = 0
if n == 0:
    count += 1
if n % 2 != 0:
    for i in range(1, n+1):
        # print(i)
        if i == 1:
            count = 2
        else:
            if i % 2 != 0:
                count += count
            if i % 2 == 0:
                count += 1
if n % 2 == 0:
    for i in range(1,n+1):
        # print(i)
        if i == 1:
            count = 2
        else:
            if i % 2 != 0:
                count += count
            if i % 2 == 0:
                count += 1
print(count)
