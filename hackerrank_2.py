l1 = [3, 4
]
l2 = [38, 48]
nl1 = []

for var in l1:
    for i in range(1, var+1):
        if var % i == 0:
            nl1.append(i)

print("Factors of 1st aaray  %s " % nl1)

nl2 = []
for j in l2:
    for i in range(1, j+1):
        if j % i == 0:
            nl2.append(i)
print("factor of second array : %s " % nl2)

unique_set1 = set(nl1)
unique_set2 = set(nl2)
unique_set = unique_set1 & unique_set2
factor_of_both_arr = list(unique_set)
print("factors that satisfy both array : %s" % factor_of_both_arr)

unique_list1 = list(unique_set1)
unique_list2 = list(unique_set2)

print("array 1  : %s " % l1)
print("array 2  : %s " % l2)

print("array 1 factor : %s " % unique_list1)
print("array 2 factor : %s " % unique_list2)


a =l1[-1]
b = l2[-1]
print(b)
print(a)
ll= []
lll =[]
for i in range(a, b, a):
    ll.append(i)
print(ll)


s=[]
l=min(l2)
for i in l1 :
    for j in range (2,1000):
        if i*j<=l:
            s.append(i*j)

all_divisible = []
for i in range(len(s)):
    for j, k in zip(l1, l2):
        if s[i] % j == 0 and k % s[i] == 0:
            all_divisible.append(s[i])

all_divisible_set = set(all_divisible)
new_list = list(all_divisible_set)
print(new_list)
print(len(new_list))



# ------ casvo code

print("------------------Pro-code-------------")


print(s)


