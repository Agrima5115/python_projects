print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input ("What percentage of tip would you like to give? 10, 12, or 15? ")
t = (100 + int(tip))/100
person = input("How many people to split the bill? ")
amt = (float(bill)/int(person)) * t
print("Each person should pay: $",format(amt,".2f"))