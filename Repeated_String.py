
a = "afcfffaged"
n = 
n_s = ""
# l = []
# while True:
#     n_s += a
#     if len(n_s) >= n:
#         break
# l.append(n_s)
# print(l)

# counter = 0
# for i in range(n):
#     if n_s[i] == "a":
#         counter += 1
# print(counter)
print(n%len(a))
print(int(a.count("a")*(n/len(a)+a.count("a"))))
