# n = int(input())
# integer_list = map(int, input().split())
# print(hash(tuple(integer_list)))


print("Enter the number of the elements in array :")
n = int(input())
print("Enter the array elements : ")
l2 = []
for i in range(n):
    l2.append(input())
print(l2)
l = []
for i in range(n):
    l.append([])

for i in range(len(l2)):
    for j in l2[i]:
        l[i].append(ord(j))

print(l)
l3 = []
for i in l:
    l3.append(sum(i))
print(l3)

l4 = []
for i in l3:
    l4.append(i % n)
print(l4)
# print(sum(l))
# print(len(l))

# print(sum(l) % len(l))
# print(279 % 11)
