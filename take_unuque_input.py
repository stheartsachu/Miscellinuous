n1 = list(map(int, list(set(input().split()))))
n2 = list(map(int, list(set(input().split()))))
from itertools import product
res = list(product(n1, n2))
# print(tuple(res))

for i in tuple(res):
    print(i, end=" ")
