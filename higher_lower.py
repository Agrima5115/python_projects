import random
import os
from higher_lower_art import logo, vs
print(logo)
from higher_lower_data import data

b = random.choice(data)
score = 0
continue_game = True

while continue_game:
  a = b
  a = random.choice(data)

  if(a == b):
    b = random.choice(data)
    
  def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"
    
  print(f"Compare A: {format_data(a)}.")
  print(vs)
  print(f"Against B: {format_data(b)}.")
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  a_follow_count = a["follower_count"]
  b_follow_count = b["follower_count"]
  
  def check(guess, a_follow_count, b_follow_count):
    # ans = max(af,bf)
    # if(guess == 'a'):
    #   guessf = a_follow_count
    # else:
    #   guessf = b_follow_count
  
    # if(guessf == ans):
    #   return True
    if(a_follow_count>b_follow_count):
      return guess == 'a'
    else:
      return guess == 'b'
  is_correct = check(guess,a_follow_count,b_follow_count)

  os.system('cls||clear')
  print(logo)
  
  if is_correct:
    score = score + 1
    print(f"You're right! Current score: {score}.")
  else:
    print(f"You're Wrong! Final Score: {score}.")
    score = 0