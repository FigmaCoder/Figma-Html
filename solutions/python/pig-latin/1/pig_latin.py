def translate(text):
    vowels = ("a", "e", "i", "o", "u")
    result = []

    for word in text.split():

        # Rule 1
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            result.append(word + "ay")
            continue

        # Rule 3
        if "qu" in word:
            qu_index = word.index("qu")
            prefix = word[:qu_index]

            if qu_index == 0 or all(c not in vowels for c in prefix):
                result.append(word[qu_index + 2:] + word[:qu_index + 2] + "ay")
                continue

        # Rules 2 and 4
        for i, char in enumerate(word):
            if char in vowels or (char == "y" and i != 0):
                result.append(word[i:] + word[:i] + "ay")
                break

    return " ".join(result)