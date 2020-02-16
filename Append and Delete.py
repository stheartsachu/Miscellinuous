s = "y"
t = "yu"
k = 2
if s.count(s[0]) == len(s) and t.count(t[0]) == len(t)or s == t and len(s) < len(t):
    print("yes")
elif len(t) > len(s):
    if len(t)+len(s) <= k:
        print("Yes")
    else:
        print("No")
else:
    n_s = []
    n_t = []
    same_word = []
    counter1 = 0
    counter2 = 0
    for i in s:
        n_s.append(i)
    for i in t:
        n_t.append(i)
    for i, j in zip(n_s, n_t):
        if i == j:
            same_word.append(i)
        if i != j:
            break
    for i in range(len(same_word), len(n_s)):
        counter1 += 1
    for i in range(len(same_word), len(n_t)):
        counter2 += 1
    if counter1+counter2 <= k:
        print("Yes")
    else:
        print("No")
