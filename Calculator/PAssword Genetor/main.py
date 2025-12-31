import random
print("Welcome  To Your Password Generator")

length = int(input("Enter the length of the password: "))

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"

number = int(input("Enter the number of passwords to generate: "))

number_of_passwords = []

for n in range(number):
    password = ''.join(random.choice(chars) for _ in range(length))
    number_of_passwords.append(password)


print("Here are your passwords:")
for pwd in number_of_passwords:
    print(pwd)
