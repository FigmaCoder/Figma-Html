import string
def is_pangram(sentence):
    letters = set(letter.lower() for letter in sentence if letter.isalpha())
    return letters >= set(string.ascii_lowercase)