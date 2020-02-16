n = 5
p = 5
book_page = []
for i in range(1, n+1):
    book_page.append(i)
if n % 2 == 0:
    book_page.append(book_page[-1])

print(book_page)
front_side = []
counter1 = 0
for i in range(0, p):
    counter1 += 1
    print(i)
    front_side.append(book_page[i])
back_side = []
counter2 = 0
for i in range(p, len(book_page)):
    back_side.append(book_page[i])
    counter2 += 1

print(front_side)
print(back_side)

print(counter1, counter2)

t_count1 = int(counter1 / 2)

t_count2 = int(counter2 / 2)

print(t_count1, t_count2)
if n == p:
    print(0)
else:
    if t_count1 < t_count2:
        print(t_count1)
    if t_count1 > t_count2:
        print(t_count2)
