s = "123"
print(s.isalnum())
for i in s:
    if i.isdigit() == True:
        print(True)
        break
    elif i.isalpha() == True:
        print(True)
        break

for i in s:
    try:
        if i.isalpha() == True:
            print(True)
            break
    finally:
        print(False)
    # else:
    #     print(False)
    #     break

for i in s:
    try:
        if i.isalpha() == True:
            print(True)
            break
    finally:
        print(False)
        break

for i in s:
    try:
        if i.isdigit() == True:
            print(True)
            break
    finally:
        print(False)
        break

for i in s:
    try:
        if i.islower() == True:
            print(True)
            break
    finally:
        print(False)
        break

for i in s:
    try:
        if i.isupper() == True:
            print(True)
            break
    finally:
        print(False)
        break


# first = []
# for i in s:
#     first.append(i)
# print(first)
#
# if s.isalnum() == True:
#     print(True)
# # else:
# #     print(False)
# # if s.isalnum() == False:
# #     print(False)
#
# if s.isalpha() == True:
#     print(True)
# if s.isalpha() == False:
#     print(False)
# if s.isdigit() == True:
#     print(True)
# if s.isdigit() == False:
#     print(False)
# if s.islower() == True:
#     print(True)
#
# if s.islower() == False:
#     print(False)
# if s.isupper() == True:
#     print(True)
# if s.isupper() == False:
#     print(False)
# if s.isalpha() == True:
#     print(True)
#
# if s.isalpha() == False:
#     print(False)
#
