c=[0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0, 1 ,0 ,1 ,0, 1, 0 ,1, 0, 0, 0 ,1, 0 ,0 ,0 ,0 ,0, 1, 0 ,1 ,0 ,1, 0, 0 ,1 ,0, 1, 0 ,1 ,0 ,0, 1 ,0 ,0 ,0 ,0 ,1 ,0, 0,1 ,0, 0,0 ,1 ,0 ,0 ,1, 0 ,1 ,0]
# c = [0 ,0 ,1 ,0 ,0 ,1 ,0]
# c = [0 ,0 ,0 ,0 ,1 ,0]
count = 0
for i in range(0,len(c),2):
    print(i)
    if c[i] == 0:
        count += 1
    if c[i] == 1:
        count += 2
print(count)

