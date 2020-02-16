s = "ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq"
n_r = []
for i in s[::-1]:
    n_r.append(ord(i))

print(n_r)
diff1 = []
for i in range(len(n_r)-1):
    diff1.append(abs(n_r[i]-n_r[i+1]))
print(diff1)
n_r1 = n_r[::-1]
print(n_r1)
diff2 = []
for i in range(len(n_r1)-1):
    diff2.append(abs(n_r1[i]-n_r1[i+1]))
if diff1 == diff2:
    print("Funny")
else:
    print("Not Funny")
