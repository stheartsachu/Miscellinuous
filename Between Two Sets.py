# Python Program to find the factors of a number

# define a function
l1 = []
def print_factors(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           l1.append(i)

# change this value for a different result.
num = 320

# uncomment the following line to take input from the user
#num = int(input("Enter a number: "))

print_factors(num)
print(l1)
