import random 

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
print("You got it!")
print("Congratulations! You've guessed the number.")

print(f"The number was: {number}")
print(f"You guessed it in {abs(guess - number)} attempts.")
print("Thanks for playing!")
print("Game Over.")
print("Goodbye!")
print("Well done!")
print("Try again soon!")
print("Perfect Guess!")
