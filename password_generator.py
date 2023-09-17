import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
randl = ""
for i in range(0,nr_letters):
  randl += random.choice(letters)
for i in range(0, nr_symbols):
  randl += random.choice(symbols)
for i in range(0,nr_numbers):
  randl += random.choice(numbers)
print(randl)

#Hard Level - Order of characters randomised:
rands = []
for i in range(0,nr_letters):
  rands.append(random.choice(letters))
for i in range(0, nr_symbols):
  rands.append(random.choice(symbols))
for i in range(0,nr_numbers):
  rands.append(random.choice(numbers))
random.shuffle(rands)
pwd = ""
for i in rands:
  pwd = pwd + i
print(pwd)  
  