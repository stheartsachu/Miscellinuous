s = "123"
n_s = ''.join(e for e in s if e.isalnum()).split()
print(n_s)
if len(n_s) != 0:
    print(True)
if len(n_s) == 0:
    print(False)

a_s = "".join(i for i in s if i.isalpha()).split()
print(a_s)
if len(a_s) != 0:
    print(True)
if len(a_s) == 0:
    print(False)

d_s = "".join(i for i in s if i.isdigit()).split()
print(d_s)
if len(d_s) != 0:
    print(True)
if len(d_s) == 0:
    print(False)

l_s = "".join(i for i in s if i.islower()).split()
print(l_s)
if len(l_s) != 0:
    print(True)
if len(l_s) == 0:
    print(False)
#
# u_s = "".join(i for i in s if i.isupper()).split()
# print(u_s)
# if len(u_s) != 0:
#     print(True)
# if len(u_s) == 0:
#     print(False)
