password = "4700"
n = len(password)
numbers = "0123456789" # password must contain a digit
lower_case = "abcdefghijklmnopqrstuvwxyz" # password must have lower case letter
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # password must contain upper case letter
special_characters = "!@#$%^&*()-+" # password must contain special characters

num = 0
l_case = 0
u_case = 0
s_case = 0
ar = [0, 0, 0, 0]  # ["digit","lower-case","upper-case","special-character"]
for i in password:
    if i in numbers:
        ar[0] += 1
    if i in lower_case:
        ar[1] += 1
    if i in upper_case:
        ar[2] += 1
    if i in special_characters:
        ar[3] += 1
print(ar)
if n < 6:
    r_l = 6-n

    # print(r_l)
    r_c = ar.count(0)
    # print(r_c)
    if r_c > r_l:
        print(r_c)
    else:
        n_p_s = r_c
        # print(n_p_s)
        # print(n_p_s)
        while True:
            if n_p_s == r_l:
                break
            n_p_s += 1
        print(n_p_s)

else:
    print(ar.count(0))
