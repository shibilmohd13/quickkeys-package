import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def _create_otp(number_of_numbers):
    otp = []
    for number in range(number_of_numbers):
        otp.append(random.choice(numbers))

    otp_final = ""
    for i in otp:
        otp_final += i

    return otp_final

def four_digit_otp():
    return _create_otp(4)

def six_digit_otp():
    return _create_otp(6)

# print(four_digit_otp())
# print(six_digit_otp())