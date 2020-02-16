a = 3
b = 9
import math
counter = 0
for i in range(a, b+1):
    # print(i)
    j = 2
    factor_len = 0
    n = i
    # print(n)
    while j * j <= n:
        if n % j:
            j += 1
        else:
            n //= j
            factor_len += 1
    if n > 1:
        factor_len += 1
    # print(factor_len)
    if factor_len % 2 == 0:
        print(factor_len)
        var = math.sqrt(i)
        if var.is_integer() == True:
            counter += 1
# print(counter)
