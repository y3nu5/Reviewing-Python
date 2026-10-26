import random

Player_Choose = int(input("What do you choose?, Type 0 for rock, 1 for paper, 2  for scissors.\n"))


rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

Choice = [rock, paper, scissors]

print(Choice[Player_Choose])

Computer_Choose = random.randint(0,2)
print("Computer Choose : ",Choice[Computer_Choose])

if Player_Choose == 0 and Computer_Choose == 0:
    print("Draw")
elif Player_Choose == 0 and Computer_Choose == 1:
    print("You Lose")
elif Player_Choose == 0 and Computer_Choose == 2:
    print("You Win")
elif Player_Choose == 1 and Computer_Choose == 0:
    print("You Win")
elif Player_Choose == 1 and Computer_Choose == 1:
    print("Draw")
elif Player_Choose == 1 and Computer_Choose == 2:
    print("You Lose")
elif Player_Choose == 2 and Computer_Choose == 0:
    print("You Lose")
elif Player_Choose == 2 and Computer_Choose == 1:
    print("You Win")
else:
    print("Draw")