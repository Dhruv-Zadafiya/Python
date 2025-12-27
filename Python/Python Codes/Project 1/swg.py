import random


choices = ["snake", "water", "gun"]
win_conditions = {
    ("snake", "water"): "You Win!  drinks ",
    ("gun", "snake"): "You Win!  kills ",
    ("water", "gun"): "You Win!  douses ",
}

user_choice = input("Enter your choice (snake / water / gun): ").strip().lower()

if user_choice not in choices:
    print(" Invalid input! Please enter 'snake', 'water', or 'gun'.")
else:
    computer_choice = random.choice(choices)

    print(f"\n🧍 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a Draw.")
    elif (user_choice, computer_choice) in win_conditions:
        print("✅ " + win_conditions[(user_choice, computer_choice)])
    else:
        print("❌ You Lose!")

    print("\n🎮 Thanks for playing!")
