s = "asvkugfiugsalddlasguifgukvsa"
alphabet_char = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# n_s = sorted(set(s))
# print(n_s)
n_s = s
arr = []
for i in n_s:
    arr.append(alphabet_char.index(i))
ar = []
for i in n_s:
    var1 = alphabet_char.index(str(i))
    # print(var1)
    var = s.count(i)
    alphabet_count.insert(var1,var)
    ar.append([i, var])
print(ar)

n_arr = sorted(arr)
print(n_arr)
counter = 0
res = []
for i in range(len(n_arr)-1):
    if n_arr[i+1]-n_arr[i] == 1:
        counter += 1
        print(counter)
        res.append(alphabet_count[n_arr[i]]+alphabet_count[n_arr[i+1]])
    if counter == 0:
        print(0)
print(alphabet_count)
print(res)
print(max(res))

# for i in range(26):
#     if alphabet_count[i] != 0 and alphabet_count[i+1] != 0:
#         print(alphabet_count[i],alphabet_count[i+1])
