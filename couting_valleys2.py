s = "UDUUUDUDDD"
length = len(s)-1
n_s = []
counter = 0
valley = 0
for i in range(1, length):
    n_s.append(s[i])
print(n_s)
for i in n_s:
    print(i)
    if i == "U":
        counter += 1
        if counter == 0:
            valley += 1
    if i == "D":
        counter -= 1
print(counter)

# counter = 0
# valley = 0
# for i in s:
#     print(i)
#     if i == "U":
#         counter += 1
#         if counter == 0:
#             valley += 1
#     else:
#         counter -= 1
# print(valley)

