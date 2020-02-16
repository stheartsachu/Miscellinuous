print("Enter a string :")
n = input()
l = []
def fun(n,l):
    for i in n:
        if i.islower() == True:
            l.append(i.upper())
        if i.isupper() == True:
            l.append(i.lower())
        if i.islower() == False and i.isupper() == False:
            l.append(i)
    str1 = ''.join(l)
    return print(str1)

l2 = [123123,123123,231,212,3,123,]

st = "".join(map(str,l2))
print(type(int(st)))
