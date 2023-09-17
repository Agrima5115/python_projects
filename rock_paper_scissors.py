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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
comp_score = 0
user_score = 0
n = int(input("How many rounds would you like to play?: "))
a = input("Enter your name: ")
for  i in range(n): 
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

    if(user_choice == 0):
        print(rock)
    elif(user_choice == 1):
        print(paper)
    elif(user_choice == 2):
        print(scissors)
    else:
        print("Invalid Choice")

    comp_choice = random.randint(0,2)
    if(comp_choice == 0):
        print(rock)
    elif(comp_choice == 1):
        print(paper)
    else:
        print(scissors)

    if((user_choice == 0 and comp_choice == 0) or (user_choice == 1 and comp_choice == 1) or (user_choice == 2 and comp_choice == 2)):
        print("Draw")
        n = n + 1
    elif((user_choice == 0 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1) or (user_choice == 1 and comp_choice == 0)):
        print("You Win")
        n = n + 1
        user_score = user_score + 1
    elif((user_choice == 0 and comp_choice == 1) or (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 0)):
        print("You Lose")
        n = n + 1
        comp_score = comp_score + 1
    else:
        print("Invalid")  

print(f"Your score is: {user_score}")
print(f"Computer's score is: {comp_score}")
print("FINAL RESULTS!!!")
if(user_score > comp_score):
    print(f"{a} is the WINNER!")
elif(comp_score > user_score):
    print("You Lose! Better luck next time.")   
else:
    print("Oops! It's a DRAW!")
