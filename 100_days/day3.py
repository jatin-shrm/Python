#Password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
n_letters=int(input("How many letters would you like in your password?\n"))
n_symbols=int(input("How many symbols would you like?\n"))
n_numbers=int(input("How many numbers would you like?\n"))
password=[]

for i in range(n_letters):
    element=random.choice(letters)
    password.append(element)
for i in range(n_symbols):
    element=random.choice(symbols)
    password.append(element)
for i in range(n_numbers):
    element=random.choice(numbers)
    password.append(element)
random.shuffle(password)
str1=""
print(str1.join(password))