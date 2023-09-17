import os
print("Welcome to the auction!")
bids = {}
bid_finished = False

def highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bid_finished:
  name = input("What is your name?")
  price = int(input("What is your bid? $"))
  bids[name] = price
  bid_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
  if(bid_continue) == "no":
    bid_finished = True
    highest_bidder(bids)
  elif bid_continue == 'yes':
    os.system('cls||clear')
    
  
  
