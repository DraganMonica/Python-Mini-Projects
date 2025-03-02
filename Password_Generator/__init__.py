import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# alege cate elemente am pus eu sa fie alese
random_nr_letters = random.choices(letters, k=nr_letters)
random_nr_symbols = random.choices(numbers, k=nr_numbers)
random_nr_numbers = random.choices(symbols, k=nr_symbols)

# populez o lista cu toate aceste elemente
password_list = []
password_list.extend(random_nr_letters)
password_list.extend(random_nr_symbols)
password_list.extend(random_nr_numbers)

# dam aici un print sa vedem lista
print(password_list)

# amesteca lista
random.shuffle(password_list)
print(password_list)

# Convertește lista într-un șir de caractere (string)
password = ''.join(password_list)

# Afișează parola generată
print(f"Your generated password is: {password}")