x = 1
y = 3
z = 2

if x < z and y < z:
    counter1 = 0
    counter2 = 0
    for i in range(x, z):
        counter1 += 1
    for i in range(y, z):
        counter2 += 1

    if counter1 < counter2:
        print("Cat A")
    if counter1 > counter2:
        print("Cat B")
    if counter1 == counter2:
        print("Mouse C")

if x < z and y > z:
    counter1 = 0
    counter2 = 0
    for i in range(x, z):
        counter1 += 1
    for i in range(y, z, -1):
        counter2 += 1

    if counter1 < counter2:
        print("Cat A")
    if counter1 > counter2:
        print("Cat B")
    if counter1 == counter2:
        print("Mouse C")
if x > z and y > z:
    counter1 = 0
    counter2 = 0
    for i in range(x, z,-1):
        counter1 += 1
    for i in range(y, z,-1):
        counter2 += 1

    if counter1 < counter2:
        print("Cat A")
    if counter1 > counter2:
        print("Cat B")
    if counter1 == counter2:
        print("Mouse C")

