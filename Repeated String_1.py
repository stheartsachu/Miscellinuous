s = "afcfffaged"
n = 962645758455
first_count = s.count("a")
last_remaining = n % len(s)
n_s = 0
if n % len(s) == 0:
    n_s = s[0:last_remaining].count("a")
print(n_s)

import math
res = first_count*(n/len(s))
print(math.ceil(res+n_s))

# ln_s = len(s)
# print(ln_s)
# new_n = 10
# ln_n = len(str(new_n))
# var = (ln_n-ln_s/2)
# print(ln_n)
#
# # counter2 = len(s)
# # while True:
# #     counter2 += len(s)
# #     # print(counter2)
# #     if counter2 > new_n:
# #         break
# # print(counter2)
# import math
# res = s.count("a")*(new_n//len(s))
# print(res)
#
# res2 = new_n % res
# print(res2)
# if res2 % 2 == 0:
#     res += 2
# else:
#     res += 1
#
# print(res)
#
#
# if ln_n % 2 != 0 and ln_s % 2 == 0:
#     res = (s.count("a")*(new_n//len(s)))
# if ln_n % 2 == 0 and ln_s % 2 == 0:
#     res = (s.count("a")*(new_n//len(s)))
#
# counter = 0
# l_s = []
# for i in range(ln_s, ln_n):
#     counter += 1
#     if counter == ln_s:
#         counter = 0
#     var = s[counter-1]
#     l_s.append(str(var))
# n_s = "".join(l_s)
# f_s = s+n_s
# print(f_s)
# counter1 = f_s.count("a")
# import math
# print(math.ceil(counter1*(new_n//len(s))))

# res = s.count("a")*(554045874191)
#
# print(res)
# print(len(str(res)))
# print(len(str(138511468548)))
#
# n = int(new_n // len(s))
# print(n)
# if len(s) == 1 and s.count("a") == 1:
#     print(n)
# else:
#     first_count = s.count("a")
#     i = 0
#     counter = 0
#     while True:
#         i += len(s)
#         counter += 1
#         if i >= n:
#             break
#     if i > n:
#         i -= len(s)
#         counter -= 1
#     res = first_count * counter
#     j = i
#     counter2 = -1
#     while True:
#         j += 1
#         counter2 += 1
#         if s[counter2] == "a":
#             res += 1
#         if j == n:
#             break
#     print(res*len(s))
