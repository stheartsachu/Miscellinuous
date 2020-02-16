s="aaabccddd"
string = []

count = []

for i in s:
    string.append(i)
print(string)

unique_string = (set(string))
print(unique_string)

for i in unique_string:
    var = [i, string.count(i)]
    count.append(var)
sorted(count, key=lambda x: x[0])
print(count)

new_count = []
for i in range(len(count)):
    if count[i][1] % 2 != 0:
        new_count.append(count[i])
# sorted(new_count, key = lambda x: x[0])
print(new_count)

final_string = []
print(final_string)

for i in range(len(new_count)):
    final_string.append(new_count[i][0])
st = "".join(sorted(final_string))

if len(new_count) == 0:
    print("Empty String")
else:
    print(st)

st = []
test = []
for i in range(len(string)-1):

    if string[i] == string[i+1]:
        test.append(string[i])
        var = [string[i], string[i+1]]
        st.append(var)

print(st)
print(test)
