d1 = 1
m1 = 1
y1 = 2015
# 31 12 2014
d2 = 31
m2 = 12
y2 = 2014
if y1 < y2 and m1 < m2:  # if return year is less than due year then, return 0 or return month is less than due month then then we return 0
    print(0)
if y1 > y2:  # if return year is greater than the due date year then, there will be fine of 10000 R
    print(10000)
if m1 > m2 and y1 == y2:  # if return date month is greater than due date month then there would be fine according to the given condition
    print (500*abs(m1-m2))
if m1 == m2 and y1 == y2:  # if return date month is equal to the  due date month then there would be fine according to the given condition
    if d1 > d2:
        print(15*abs(d1-d2))
    if d1 <= d2 :
        print(0)
print()
