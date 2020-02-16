i = 1
j = 2000000
k = 1000000000

days = []
for l in range(i, j+1):
    days.append(l)

mirror = []
for i in range(len(days)):
    mirror.append([])

for m in range(len(days)):
    string = "%s" % days[m]
    for n in string:
        mirror[m].append(n)

new_mirror = []
for i in mirror:
    new_mirror.append(i[::-1])

final = []
for i in new_mirror:
    final.append("".join(i))

last = []
for i, z in zip(days, final):
    var = int(i)
    var1 = int(z)
    var3 = abs(var-var1)/k
    
    if var3.is_integer() == True:
        last.append(var3)

print(len(last))
import time
start_time = time.time()
print(start_time)
