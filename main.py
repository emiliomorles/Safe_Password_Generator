#Safe Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

password_list = []
# number_of_letters = nr_letters
for character in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
  
for character in range(1, nr_numbers + 1):
  random_character = random.choice(numbers)
  password_list += random_character
  
for character in range(1, nr_symbols + 1):
  random_character = random.choice(symbols)
  password_list += random_character

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for character in password_list:
  password += character

print(f"Your password is {password}")
# random_letters = random.randint(1, 52) 
# print(letters[random_letters]) 
# random_letters = random.sample(letters, nr_letters - 1)
# for letter in random_letters:
#   print(letter)