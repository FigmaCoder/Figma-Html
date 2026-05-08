"""Rotational cipher implementation."""


def rotate(text, key):
    """Rotate letters in text by the given key."""

    result = []

    for character in text:

        if character.islower():
            rotated = chr((ord(character) - ord('a') + key) % 26 + ord('a'))
            result.append(rotated)

        elif character.isupper():
            rotated = chr((ord(character) - ord('A') + key) % 26 + ord('A'))
            result.append(rotated)

        else:
            result.append(character)

    return "".join(result)