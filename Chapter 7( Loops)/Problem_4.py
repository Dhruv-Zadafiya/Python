n = int(input("Enter a number: "))
product=1


for i in range(1, n+1):
    product= product * i
print(f"The product of {n} is {product}")


for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

sum=0

for i in range(1, n+1):
    sum= sum + i
print(f"The sum of first {n} natural numbers is {sum}")
for i in range(1, n+1):
    if i%2!=0:
        print(i, end=" ")
for i in range(1, n+1):
    if i%2==0:
        print(i, end=" ")
factorial=1
for i in range(1, n+1):
    factorial= factorial * i
print(f"The factorial of {n} is {factorial}")


for i in range(1, n+1):
    if n%i==0:
        print(i, end=" ")
for i in range(1, n+1):
    if n%i!=0:
        print(i, end=" ")
count=0
for i in range(1, n+1):
    if n%i==0:
        count+=1
print(f"The number of factors of {n} is {count}")
print(f"The factors of {n} are: ", end="")


for i in range(1, n+1):
    if n%i==0:
        print(i, end=" ")
print()
if count==2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")