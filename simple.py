import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

guesses = 0
guess = -1

print("Welcome to the Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it!")

while guess != number:
    guess = int(input("Guess the number: "))
    guesses += 1   # ✅ Only one increment here

    if guess < number:
        print("Too low! Try a higher number.")
    elif guess > number:
        print("Too high! Try a lower number.")
    else:
        print(f"🎉 Correct! You guessed the number {number} in {guesses} attempts.")
        print("Thank you for playing!")
