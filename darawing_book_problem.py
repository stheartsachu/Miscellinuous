n = 5
p = 4
book_pages = []
for i in range(1, n+1):
    book_pages.append(i)
print(book_pages)

first_side = []

for i in range(p):
    # if i != len(book_pages)-1:
        first_side.append(book_pages[i])

print(first_side)
var = int(len(first_side)/2)
print(var)

no_turn_fs = len(first_side)-1

back_Side = []
for i in range(p, n):
    back_Side.append(book_pages[i])
var2 = int(len(back_Side)/2)

no_turn_bs = len(back_Side)-1

# print(var)
print(var2)

#
# print(len(first_side))
# print(len(back_Side))
if len(back_Side) == 1 and var2 == 0:
    print(len(back_Side))
else:
    if var > var2 :
        print(var2)
    if var < var2:
        print(var)
    if var == var2:
        print(var)

