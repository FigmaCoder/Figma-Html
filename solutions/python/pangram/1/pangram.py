import string
def is_pangram(sentence):
    letters = set(c.lower() for c in sentence if c.isalpha())
    return letters >= set(string.ascii_lowercase)