print("Enter a number :")
n = int(input())
counter = 0
if n == 0:
    print(1)
else:
    for i in range(n):
        counter += 2
        print()
        # for j in range(n):
        #     print(2)
print(counter)
