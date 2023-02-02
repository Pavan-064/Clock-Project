# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

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

human = int(input("Enter ur number of choice,\n0:rock\n1:paper\n2:scissors\n"))

if human == 0:
    print(rock)
elif human == 1:
    print(paper)
elif human == 2:
    print(scissors)


import random
comp = random.randint(0,2)

print("Computer choose:")


if comp == 0:
    print(rock)
elif comp == 1:
    print(paper)
elif comp == 2:
    print(scissors)


if human == 0:
    if comp == 0:
        print("Tie")
    elif comp == 1:
        print("Computer wins and U lose")
    else:
        print("You win")

if human == 1:
    if comp == 0:
        print("You win")
    elif comp == 1:
        print("Tie")
    else:
        print("Computer wins and U lose")

if human == 2:
    if comp == 0:
        print("Computer wins and U lose")
    elif comp == 1:
        print("You win")
    else:
        print("Tie")
