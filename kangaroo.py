x1 = 0
v1 = 3
x2 = 4
v2 = 2

# def fun(f_kan,s_kan):
#     if f_kan == s_kan:
#         return True
# print(fun(f_kan,s_kan))
# while fun(f_kan,s_kan) == True:
#
#     f_kan = f_kan+v1
#     print(f_kan)

f_kan = x1
s_kan = x2
while(f_kan <= 10000 and s_kan <= 10000 ):
    f_kan += v1
    s_kan += v2
    # try:
    if f_kan == s_kan:
        print("YES")
        break
    # finally:
    #         print("NO")
    #         break
else:
    print("NO")

