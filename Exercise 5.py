import random


print("Welcome to the Snake, Water, Gun game!")

print("Choose your option:")
print("1: Snake")
print("2: Water")
print("3: Gun")
user = int(input("Enter your choice (1/2/3): "))


if user not in [1, 2, 3]:
    print("Invalid choice! Please enter 1, 2, or 3.")
else:

    comp = random.randint(1, 3)


    choices = {1: "Snake", 2: "Water", 3: "Gun"}
    print(f"You chose: {choices[user]}")
    print(f"Computer chose: {choices[comp]}")


    if user == comp:
        print("It's a draw!")
    elif (user == 1 and comp == 2) or (user == 2 and comp == 3) or (user == 3 and comp == 1):
        print("You win!")
    else:
        print("You lose!")
