# y = 23
# a = "{:.2f}".format(y)
# print(a)
# a = input()
# print(a.split())
import numpy
n = input().split()
n_l = []
for i in n:
    n_l.append(float(i))
print(numpy.polyval(n_l, int(input())))
