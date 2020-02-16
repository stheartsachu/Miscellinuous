ll = [["wqw","wqwwqw"],["1212"]]
print("Enter the Number of Entries")
n1 = int(input())
d = {}
l = []
for i in range(n1):
    inpt = input().split()
    d.update({""%(inpt[0]):""%()})
print(l)
l2 = {}
for i in l:
    if len(i[0]) == 0 or len(i[1]) == 0:
        print("Not found")
    else:
        var1 = i[0]
        var2 = i[1]
        print("%s=%s"%(var1,var2))

