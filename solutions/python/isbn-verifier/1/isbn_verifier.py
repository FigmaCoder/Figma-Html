def is_valid(isbn):
    # Remove hyphens
    isbn = isbn.replace("-", "")

    # Must be exactly 10 characters
    if len(isbn) != 10:
        return False

    digits = []

    for i, char in enumerate(isbn):

        # X is only allowed as the last character
        if char == "X":
            if i != 9:
                return False
            digits.append(10)

        elif char.isdigit():
            digits.append(int(char))

        else:
            return False

    total = sum(d * (10 - i) for i, d in enumerate(digits))

    return total % 11 == 0