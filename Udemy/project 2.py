# Rock Paper Scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_pos = [rock, paper, scissor]
user = int(input("Choose 0.Rock; 1;Paper; 2.Scissor: "))
comp = random.randint(0,2)

if user == 0 and comp == 2:
    print(f"You choose: {game_pos[user]}")
    print(f"Computer choose: {game_pos[comp]}")
    print("You Win!")
elif comp == 0 and user == 2:
    print(f"You choose: {game_pos[user]}")
    print(f"Computer choose: {game_pos[comp]}")
    print("You Lose!")
elif comp > user :
    print(f"You choose: {game_pos[user]}")
    print(f"Computer choose: {game_pos[comp]}")
    print("You  Lose!!!")
elif comp == user:
    print(f"You choose: {game_pos[user]}")
    print(f"Computer choose: {game_pos[comp]}")
    print("Its Draw")
elif user > comp:
    print(f"You choose: {game_pos[user]}")
    print(f"Computer choose: {game_pos[comp]}")
    print("You Win!!")
else:
    print("You enter wrong input...")

