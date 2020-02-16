x = 22
y = 70
z = 75

counter1 = 0
counter2 = 0
if z > x and z > y:
    for i in range(x, z):
        counter1 += 1
    for i in range(y, z):
        counter2 += 1

if z < x and z < y:
    for i in range(x, z,-1):
        counter1 += 1
    for i in range(y, z, -1):
        counter2 += 1

if x < z and z < y:
    for i in range(x, z):
        counter1 += 1
    for i in range(y, z, -1):
        counter2 += 1

print(counter2)
print(counter1)

if counter1 < counter2:
    print("Cat A")
if counter1 > counter2:
    print("Cat B")
if counter1 == counter2:
    print("Mouse C")
