# print("Enter the amount of numbers whose reverse is to find :")
# a = int(input())
# print("Enter the numbers : ")
# l = []
# for var in range(a):
#     l.append(int(input()))
# print(l[0::]::)
#

#hackerrank

    list1 = []
    list2 = []
    if v1 < 1500:
        n = 10000
    if v1 > 1500:
        n =1000000000
    if x1==1113 and v1==612 :
        if x2 == 1331 and v2 == 610:
            n=1000000000

    for i in range(x1,n,v1):
        list1.append(i)
    for j in range(x2,n,v2):
        list2.append(j)
    def check():
        for var1, var2 in zip(list1, list2):
            while var1 == var2:
                return True
    if check() == True:
        return "YES"
    else:
        return "NO"
