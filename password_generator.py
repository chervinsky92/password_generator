import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Let's generate a password!")
n_letters= int(input("How many letters would you like in your password?\n")) 
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

password = []
for letter in range(n_letters):
    password += random.choice(letters)
for symbol in range(n_symbols):
    password += random.choice(symbols)
for number in range(n_numbers):
    password += random.choice(numbers)
# print(password)

random.shuffle(password)
# print(password)
print(f'Your password is: {"".join(password)}')