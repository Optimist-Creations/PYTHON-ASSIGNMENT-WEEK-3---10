number = int(input(f"Enter any to get Factorial\n"))
Fact = 1
n = 1
while n <= number:
    Fact *= n
    n += 1
print ("Factorial of ", number, "is", Fact)