"""ISBN-10 validation module."""


def is_valid(isbn):
    """Check whether an ISBN-10 string is valid."""

    cleaned_isbn = isbn.replace("-", "")

    if len(cleaned_isbn) != 10:
        return False

    digits = []

    for position, character in enumerate(cleaned_isbn):

        if character == "X":
            if position != 9:
                return False
            digits.append(10)

        elif character.isdigit():
            digits.append(int(character))

        else:
            return False

    total = sum(
        digit * (10 - position)
        for position, digit in enumerate(digits)
    )

    return total % 11 == 0