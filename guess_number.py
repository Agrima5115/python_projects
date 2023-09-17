import random
from guess_number_logo import logo
print(logo)

easy_turns = 10
hard_turns = 5
turns = 0

# def guesses(guess,ans,turns):
#   if(guess>ans):
#     print("Try lower.")
#     return turns - 1
#   elif(guess<ans):
#     print("Try higher.")
#     return turns - 1
#   else:
#     print("Wonderful!")
#     print(f"You got it! The correct answer is : {ans}")

def guesses(guess, ans, turns):
    diff = abs(guess - ans)
    if diff == 0:
        print("Wonderful!")
        print(f"You got it! The correct answer is : {ans}")
    elif diff <= 10:
        print("You're close!")
        return turns - 1
    elif diff <= 25:
        print("You're far.")
        return turns - 1
    else:
        print("You're very far.")
        return turns - 1

def difficulty():
    mode = input("Choose difficulty level. Type 'easy' or 'hard': ")
    if(mode == "easy"):
      return easy_turns
      print("You have 10 attempts remaining to guess the number.")
    elif (mode == "hard"):
      return hard_turns
      print("You have 5 attempts remaining to guess the number.")
    else:
      print("Invalid mode")

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  ans = random.randint(1,100)
  turns = difficulty()
  guess = 0
  while guess!=ans:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Guess a number: "))
    turns = guesses(guess,ans,turns)
    if turns == 0:
      print("You lose!")
      print(f"The number was {ans}")
      return
    elif guess!=ans:
      print("Guess again.")
game()