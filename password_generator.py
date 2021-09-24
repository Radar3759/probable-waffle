#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
####
#Code above line 12 is base code provided by the project
#Code below line 13 is my code.

#create an empty str
password = ""

for letter in range(nr_letters):
  password += random.choice(letters)
  
for number in range(nr_numbers):
  password += random.choice(numbers)

for symbol in range(nr_symbols):
  password += random.choice(symbols)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print(f"\nThis is not randomised.\nIt is in order of letters, numbers, symbols: \n{password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#turn the password str into a list
p_list = list(password)
#shuffle the list
random.shuffle(p_list)
#turn the list into a str
random_password = ''.join(p_list)
#I kept the UK Enlglish spelling
print(f"\nThis is randomised: {random_password}")

