def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)

    a_number = sum(int(digit) ** power for digit in digits)
    return number == a_number
