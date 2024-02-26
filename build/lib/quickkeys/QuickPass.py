#Password Generator Project

import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def _create_password(number_of_letters, number_of_symbols, number_of_numbers):
    password = []
    for letter in range(number_of_letters):
        password.append(random.choice(letters))

    for symbol in range(number_of_symbols):
        password.append(random.choice(symbols))

    for number in range(number_of_numbers):
        password.append(random.choice(numbers))

    # shuffled password
    random.shuffle(password)

    password_final = ""
    for i in password:
        password_final += i

    return password_final

def four_digit_password():
    return _create_password(2,1,1)

def six_digit_password():
    return _create_password(4,1,1)

def eight_digit_password():
    return _create_password(4,2,2)

def strong_password():
    num_of_letters = random.randint(8, 10)
    num_of_symbols = random.randint(2, 4)
    num_of_numbers = random.randint(2, 4)

    return _create_password(num_of_letters,num_of_numbers, num_of_symbols)

