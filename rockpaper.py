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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player=input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors\n")
player=int(player)
game=[rock, paper, scissors]
if player>2:
  print("Invalid Entry!!")
  exit
print(game[player])
print("Computer chose:\n")
comp=random.randint(0,2)
print(game[comp])
if game[player]==rock:
  if game[comp]==scissors:
    print("You Win!!")
  elif game[comp]==paper:
    print("You Loose")
  else:
    print("Its a Tie")
elif game[player]==scissors:
  if game[comp]==scissors:
    print("Its a Tie")
  elif game[comp]==paper:
    print("You Win!!")
  else:
    print("You lose")
elif game[player]==paper:
  if game[comp]==scissors:
    print("You Loose")
  elif game[comp]==paper:
    print("Its a Tie")
  else:
    print("You Win!!")
else:
  print("Invalid entry")
